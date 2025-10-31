from core.customer import Customer
from core.order import Order
from utils.report import Report
from exceptions.restaurant_exceptions import FeedbackException
from datetime import datetime

class Feedback:
    def __init__(self, feedback_id: int, customer: Customer, order: Order, rating: int, comment: str):
        self.feedback_id = feedback_id
        self.customer = customer
        self.order = order
        self.rating = rating
        self.comment = comment
        self.timestamp = datetime.now()
        self.sentiment_score = 0.0
        self.is_responded = False
        self.response_text = ""
        self.tags = []


class RatingSystem:
    def __init__(self):
        self.total_ratings = 0
        self.average_rating = 0.0
        self.rating_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    def update_rating_stats(self, new_rating: int):
        self.total_ratings += 1
        self.rating_distribution[new_rating] += 1
        self.average_rating = sum(k * v for k, v in self.rating_distribution.items()) / self.total_ratings

    def get_rating_analysis(self) -> dict:
        return {
            "total_ratings": self.total_ratings,
            "average_rating": round(self.average_rating, 2),
            "distribution": self.rating_distribution,
            "rating_percentage": {k: round(v / self.total_ratings * 100, 2) for k, v in
                                  self.rating_distribution.items()}
        }


class FeedbackService:
    def __init__(self):
        self.feedback_list = []
        self.rating_system = RatingSystem()
        self.feedback_counter = 1
        self.positive_keywords = ["отлично", "прекрасно", "восхитительно", "супер", "рекомендую", "великолепно"]
        self.negative_keywords = ["ужасно", "плохо", "отвратительно", "кошмар", "разочарован"]

    def collect_feedback(self, customer: Customer, order: Order, rating: int, comment: str) -> Feedback:
        """Уникальное поведение: сбор и анализ отзыва с проверкой валидности"""
        if not (1 <= rating <= 5):
            raise FeedbackException("Рейтинг должен быть от 1 до 5")

        if len(comment) > 1000:
            raise FeedbackException("Комментарий слишком длинный")

        feedback = Feedback(self.feedback_counter, customer, order, rating, comment)
        self.feedback_counter += 1

        # Анализ тональности комментария
        feedback.sentiment_score = self._analyze_sentiment(comment)
        feedback.tags = self._extract_tags(comment)

        self.feedback_list.append(feedback)
        self.rating_system.update_rating_stats(rating)

        return feedback

    def _analyze_sentiment(self, comment: str) -> float:
        """Уникальное поведение: анализ тональности текста"""
        comment_lower = comment.lower()
        positive_count = sum(1 for word in self.positive_keywords if word in comment_lower)
        negative_count = sum(1 for word in self.negative_keywords if word in comment_lower)

        total_words = len(comment.split())
        if total_words == 0:
            return 0.5

        sentiment = 0.5 + (positive_count - negative_count) * 0.1
        return max(0.0, min(1.0, sentiment))

    @staticmethod
    def _extract_tags(comment: str) -> list:
        """Уникальное поведение: извлечение тегов из комментария"""
        tags = []
        food_keywords = ["еда", "блюдо", "кухня", "вкус", "готовка"]
        service_keywords = ["обслуживание", "официант", "сервис", "персонал"]
        atmosphere_keywords = ["атмосфера", "интерьер", "музыка", "уют"]

        comment_lower = comment.lower()

        if any(word in comment_lower for word in food_keywords):
            tags.append("food")
        if any(word in comment_lower for word in service_keywords):
            tags.append("service")
        if any(word in comment_lower for word in atmosphere_keywords):
            tags.append("atmosphere")

        return tags

    @staticmethod
    def respond_to_feedback(feedback: Feedback, response: str):
        """Уникальное поведение: ответ на отзыв"""
        if feedback.is_responded:
            raise FeedbackException("На этот отзыв уже дан ответ")

        feedback.is_responded = True
        feedback.response_text = response

    def get_feedback_by_customer(self, customer: Customer) -> list:
        """Получение отзывов конкретного клиента"""
        return [fb for fb in self.feedback_list if fb.customer.customer_id == customer.customer_id]

    def get_feedback_by_rating(self, min_rating: int, max_rating: int) -> list:
        """Фильтрация отзывов по рейтингу"""
        return [fb for fb in self.feedback_list if min_rating <= fb.rating <= max_rating]

    def generate_feedback_report(self, period: str) -> Report:
        """Уникальное поведение: генерация отчета по отзывам"""
        from utils.report import Report

        recent_feedback = self._filter_feedback_by_period(period)

        content = {
            "period": period,
            "total_feedback": len(recent_feedback),
            "average_rating": self.rating_system.average_rating,
            "rating_analysis": self.rating_system.get_rating_analysis(),
            "common_tags": self._get_common_tags(recent_feedback),
            "response_rate": self._calculate_response_rate(recent_feedback)
        }

        report = Report(len(self.feedback_list), "feedback_report", content, datetime.now())
        return report

    def _filter_feedback_by_period(self, period: str) -> list:
        """Фильтрация отзывов по периоду"""
        # Упрощенная реализация
        return self.feedback_list[-10:] if period == "recent" else self.feedback_list

    @staticmethod
    def _get_common_tags(feedback_list: list) -> dict:
        """Анализ популярных тегов"""
        tag_count = {}
        for feedback in feedback_list:
            for tag in feedback.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count

    @staticmethod
    def _calculate_response_rate(feedback_list: list) -> float:
        """Расчет процента отвеченных отзывов"""
        if not feedback_list:
            return 0.0
        responded_count = sum(1 for fb in feedback_list if fb.is_responded)
        return round(responded_count / len(feedback_list) * 100, 2)