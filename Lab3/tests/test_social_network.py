import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from users.User import User
from users.Profile import Profile
from users.PrivacySettings import PrivacySettings
from users.UserPreferences import UserPreferences
from users.UserStatistics import UserStatistics
from users.FriendRequest import FriendRequest
from users.UserAnalytics import UserAnalytics

from content.Post import Post
from content.Comment import Comment
from content.Like import Like
from content.Media import Media
from content.Hashtag import Hashtag
from content.Poll import Poll
from content.PollOption import PollOption
from content.Story import Story
from content.StoryViewer import StoryViewer
from content.Reaction import Reaction
from content.Bookmark import Bookmark
from content.ContentAnalytics import ContentAnalytics

from communication.Message import Message
from communication.Chat import Chat
from communication.ChatParticipant import ChatParticipant
from communication.Notification import Notification
from communication.Announcement import Announcement

from groups.Group import Group
from groups.GroupMember import GroupMember
from groups.GroupSettings import GroupSettings
from groups.GroupInvitation import GroupInvitation

from events.Event import Event
from events.EventAttendee import EventAttendee
from events.EventReminder import EventReminder

from system.Feed import Feed
from system.FeedAlgorithm import FeedAlgorithm
from system.Search import Search
from system.SearchIndex import SearchIndex
from system.Analytics import Analytics
from system.Moderation import Moderation
from system.ContentModeration import ContentModeration
from system.UserModeration import UserModeration
from system.Backup import Backup
from system.Report import Report

from business.Advertisement import Advertisement
from business.Subscription import Subscription
from business.Payment import Payment
from business.PremiumFeature import PremiumFeature
from business.BusinessPage import BusinessPage
from business.AiRecommendation import AiRecommendation
from business.Metrics import Metrics
from business.Scheduler import Scheduler
from business.Integration import Integration

from exceptions.UserNotFound import UserNotFound
from exceptions.UserExists import UserExists
from exceptions.InvalidCredentials import InvalidCredentials
from exceptions.PostNotFound import PostNotFound
from exceptions.PostAccessDenied import PostAccessDenied


# Fixtures
@pytest.fixture
def sample_user():
    return User("testuser", "test@example.com", "password123")


@pytest.fixture
def sample_user2():
    return User("frienduser", "friend@example.com", "password456")


@pytest.fixture
def sample_profile():
    return Profile("Test User", "Test bio", "http://avatar.com/img.jpg", "Test City")


@pytest.fixture
def sample_post(sample_user):
    return Post(sample_user, "Test post content")


@pytest.fixture
def sample_comment(sample_user):
    return Comment(sample_user, "Test comment")


@pytest.fixture
def sample_media():
    return Media("http://example.com/image.jpg", "image", size_bytes=1000)


@pytest.fixture
def sample_chat():
    return Chat("Test Chat")


@pytest.fixture
def sample_group(sample_user):
    return Group("Test Group", "Test Description", sample_user)


@pytest.fixture
def sample_event(sample_user):
    return Event("Test Event", sample_user, "Test Location", "2023-01-01")


# Tests for Users Module
class TestUser:
    def test_user_creation(self, sample_user):
        assert sample_user.username == "testuser"
        assert sample_user.email == "test@example.com"
        assert sample_user.is_active == True

    def test_user_registration(self, sample_user):
        result = sample_user.register()
        assert result["status"] == "registered"
        assert result["username"] == "testuser"
        assert sample_user.is_active == True

    def test_user_authentication_success(self, sample_user):
        result = sample_user.authenticate("password123")
        assert result["authenticated"] == True
        assert result["user"] == "testuser"

    def test_user_authentication_failure(self, sample_user):
        result = sample_user.authenticate("wrongpassword")
        assert result["authenticated"] == False

    def test_user_email_update_valid(self, sample_user):
        result = sample_user.update_email("new@example.com")
        assert result["email_updated"] == True
        assert sample_user.email == "new@example.com"

    def test_user_email_update_invalid(self, sample_user):
        original_email = sample_user.email
        result = sample_user.update_email("invalid-email")
        assert result["email_updated"] == False
        assert sample_user.email == original_email

    def test_user_deactivation(self, sample_user):
        result = sample_user.deactivate_account()
        assert result["deactivated"] == True
        assert sample_user.is_active == False

    def test_user_profile_snapshot(self, sample_user):
        snapshot = sample_user.get_profile_snapshot()
        assert "username" in snapshot
        assert "email" in snapshot
        assert "profile" in snapshot


class TestProfile:
    def test_profile_creation(self, sample_profile):
        assert sample_profile.display_name == "Test User"
        assert sample_profile.bio == "Test bio"
        assert sample_profile.avatar_url == "http://avatar.com/img.jpg"

    def test_profile_update_bio(self, sample_profile):
        result = sample_profile.update_bio("New bio text")
        assert result["bio_updated"] == True
        assert sample_profile.bio == "New bio text"

    def test_profile_change_avatar_valid(self, sample_profile):
        result = sample_profile.change_avatar("http://new.com/avatar.jpg")
        assert result["avatar_changed"] == True
        assert sample_profile.avatar_url == "http://new.com/avatar.jpg"

    def test_profile_change_avatar_invalid(self, sample_profile):
        original_avatar = sample_profile.avatar_url
        result = sample_profile.change_avatar("invalid-url")
        assert result["avatar_changed"] == False
        assert sample_profile.avatar_url == original_avatar

    def test_profile_view(self, sample_profile):
        view = sample_profile.view_profile()
        assert "display_name" in view
        assert "bio" in view
        assert "location" in view


class TestPrivacySettings:
    def test_privacy_settings_creation(self):
        privacy = PrivacySettings()
        assert privacy.profile_visible == True
        assert privacy.messages_allowed == True
        assert privacy.search_indexable == True
        assert privacy.blocked_users == []

    def test_set_profile_visibility(self):
        privacy = PrivacySettings()
        result = privacy.set_profile_visibility(False)
        assert result == False
        assert privacy.profile_visible == False

    def test_add_blocked_user(self):
        privacy = PrivacySettings()
        result = privacy.add_blocked_user("user123")
        assert result["blocked"] == True
        assert result["blocked_users_count"] == 1
        assert "user123" in privacy.blocked_users

    def test_add_duplicate_blocked_user(self):
        privacy = PrivacySettings()
        privacy.add_blocked_user("user123")
        result = privacy.add_blocked_user("user123")
        assert result["blocked"] == False

    def test_is_blocked(self):
        privacy = PrivacySettings()
        privacy.add_blocked_user("user123")
        assert privacy.is_blocked("user123") == True
        assert privacy.is_blocked("user456") == False


class TestUserPreferences:
    def test_user_preferences_creation(self):
        prefs = UserPreferences()
        assert prefs.theme == "light"
        assert prefs.notifications_enabled == True
        assert prefs.language == "en"

    def test_set_theme_valid(self):
        prefs = UserPreferences()
        result = prefs.set_theme("dark")
        assert result == "dark"
        assert prefs.theme == "dark"

    def test_set_theme_invalid(self):
        prefs = UserPreferences()
        original_theme = prefs.theme
        result = prefs.set_theme("invalid")
        assert result == original_theme

    def test_toggle_notifications(self):
        prefs = UserPreferences()
        result = prefs.toggle_notifications(False)
        assert result == False
        assert prefs.notifications_enabled == False

    def test_set_language_valid(self):
        prefs = UserPreferences()
        result = prefs.set_language("fr")
        assert result == "fr"
        assert prefs.language == "fr"

    def test_set_language_invalid(self):
        prefs = UserPreferences()
        original_language = prefs.language
        result = prefs.set_language("invalid")
        assert result == original_language


class TestUserStatistics:
    def test_user_statistics_creation(self):
        stats = UserStatistics()
        assert stats.posts_count == 0
        assert stats.followers == 0
        assert stats.following == 0
        assert stats.total_logins == 0

    def test_basic_summary(self):
        stats = UserStatistics()
        stats.posts_count = 5
        stats.followers = 100
        stats.following = 50

        summary = stats.basic_summary()
        assert summary["posts"] == 5
        assert summary["followers"] == 100
        assert summary["following"] == 50


class TestFriendRequest:
    def test_friend_request_creation(self, sample_user, sample_user2):
        friend_request = FriendRequest(sample_user, sample_user2, "Hello!")
        assert friend_request.sender == sample_user
        assert friend_request.receiver == sample_user2
        assert friend_request.status == "pending"

    def test_accept_request(self, sample_user, sample_user2):
        friend_request = FriendRequest(sample_user, sample_user2)
        friend_request.send_request()
        result = friend_request.accept_request()
        assert result["accepted"] == True
        assert result["status"] == "accepted"

    def test_decline_request(self, sample_user, sample_user2):
        friend_request = FriendRequest(sample_user, sample_user2)
        friend_request.send_request()
        result = friend_request.decline_request()
        assert result["declined"] == True
        assert result["status"] == "declined"


class TestUserAnalytics:
    def test_user_analytics_creation(self):
        analytics = UserAnalytics()
        assert analytics.recent_activity == []
        assert analytics.engagement_score == 0

    def test_get_recent_activity(self):
        analytics = UserAnalytics()
        for i in range(10):
            analytics.add_activity(f"activity_{i}")

        recent = analytics.get_recent_activity(5)
        assert len(recent) == 5

    def test_compute_growth_trend_stable(self):
        analytics = UserAnalytics(engagement_score=5)
        result = analytics.compute_growth_trend()
        assert result["trend"] == "stable"
        assert result["score"] == 5

    def test_compute_growth_trend_growing(self):
        analytics = UserAnalytics(engagement_score=15)
        result = analytics.compute_growth_trend()
        assert result["trend"] == "growing"
        assert result["score"] == 15


# Tests for Content Module
class TestPost:
    def test_post_creation(self, sample_post, sample_user):
        assert sample_post.author == sample_user
        assert sample_post.text == "Test post content"
        assert sample_post.visibility == "public"

    def test_edit_text_valid(self, sample_post):
        result = sample_post.edit_text("Updated content")
        assert result["edited"] == True
        assert sample_post.text == "Updated content"

    def test_edit_text_invalid(self, sample_post):
        original_text = sample_post.text
        result = sample_post.edit_text(None)
        assert result["edited"] == False
        assert sample_post.text == original_text

class TestComment:
    def test_comment_creation(self, sample_comment, sample_user):
        assert sample_comment.author == sample_user
        assert sample_comment.text == "Test comment"
        assert sample_comment.edited == False

    def test_update_text(self, sample_comment):
        result = sample_comment.update_text("Updated comment")
        assert result["updated"] == True
        assert sample_comment.text == "Updated comment"
        assert sample_comment.edited == True

    def test_render_preview(self, sample_comment):
        preview = sample_comment.render_preview()
        assert "testuser" in preview
        assert "Test comment" in preview


class TestLike:
    def test_like_creation(self, sample_user):
        like = Like(sample_user, "post", "post123")
        assert like.user == sample_user
        assert like.target_type == "post"
        assert like.active == True

    def test_add_like(self, sample_user):
        like = Like(sample_user)
        like.active = False
        result = like.add_like()
        assert result["liked"] == True
        assert like.active == True

    def test_remove_like(self, sample_user):
        like = Like(sample_user)
        result = like.remove_like()
        assert result["liked"] == False
        assert like.active == False

    def test_like_info(self, sample_user):
        like = Like(sample_user, "post", "post123")
        info = like.like_info()
        assert info["user"] == "testuser"
        assert info["target"] == "post123"


class TestMedia:
    def test_media_creation(self, sample_media):
        assert sample_media.url == "http://example.com/image.jpg"
        assert sample_media.media_type == "image"
        assert sample_media.processed == False

    def test_validate_upload_valid(self, sample_media):
        result = sample_media.validate_upload()
        assert result["valid"] == True
        assert result["processed"] == True

    def test_validate_upload_invalid_url(self):
        media = Media(None, "image", size_bytes=1000)
        result = media.validate_upload()
        assert result["valid"] == False

    def test_validate_upload_invalid_size(self):
        media = Media("http://example.com/image.jpg", "image", size_bytes=-1)
        result = media.validate_upload()
        assert result["valid"] == False

    def test_get_metadata(self, sample_media):
        metadata = sample_media.get_metadata()
        assert metadata["url"] == "http://example.com/image.jpg"
        assert metadata["type"] == "image"
        assert metadata["size"] == 1000


class TestHashtag:
    def test_hashtag_creation(self):
        hashtag = Hashtag("#test")
        assert hashtag.tag == "#test"
        assert hashtag.count == 0

    def test_attach_related(self):
        hashtag = Hashtag("#test")
        related_hashtag = Hashtag("#related")
        result = hashtag.attach_related(related_hashtag)
        assert result["added"] == True
        assert result["related_count"] == 1
        assert related_hashtag in hashtag.related_tags

    def test_attach_duplicate_related(self):
        hashtag = Hashtag("#test")
        related_hashtag = Hashtag("#related")
        hashtag.attach_related(related_hashtag)
        result = hashtag.attach_related(related_hashtag)
        assert result["added"] == False


class TestPoll:
    def test_poll_creation(self):
        poll = Poll("Test question?", created_at="2023-01-01")
        assert poll.question == "Test question?"
        assert poll.is_open == True


    def test_close_poll(self):
        poll = Poll("Test question?")
        result = poll.close_poll()
        assert result["closed"] == True
        assert poll.is_open == False


class TestPollOption:
    def test_poll_option_creation(self):
        option = PollOption("Option text")
        assert option.text == "Option text"
        assert option.votes == 0

    def test_option_info(self):
        option = PollOption("Option text", votes=5)
        info = option.option_info()
        assert info["text"] == "Option text"
        assert info["votes"] == 5


class TestStory:
    def test_story_creation(self, sample_user):
        story = Story(sample_user, "Story content")
        assert story.author == sample_user
        assert story.content == "Story content"

class TestStoryViewer:
    def test_story_viewer_creation(self, sample_user):
        viewer = StoryViewer(sample_user, "2023-01-01")
        assert viewer.user == sample_user
        assert viewer.viewed_at == "2023-01-01"

    def test_record_reaction(self, sample_user):
        viewer = StoryViewer(sample_user)
        result = viewer.record_reaction("like")
        assert result["saved"] == True
        assert viewer.reaction == "like"

    def test_get_view_record(self, sample_user):
        viewer = StoryViewer(sample_user, "2023-01-01")
        record = viewer.get_view_record()
        assert record["user"] == "testuser"
        assert record["viewed_at"] == "2023-01-01"


class TestReaction:
    def test_reaction_creation(self, sample_user):
        reaction = Reaction(sample_user, "like")
        assert reaction.user == sample_user
        assert reaction.reaction_type == "like"

    def test_toggle_reaction(self, sample_user):
        reaction = Reaction(sample_user, "like")
        result = reaction.toggle_reaction("love")
        assert result["changed"] == True
        assert reaction.reaction_type == "love"

    def test_toggle_reaction_same_type(self, sample_user):
        reaction = Reaction(sample_user, "like")
        result = reaction.toggle_reaction("like")
        assert result["changed"] == False

    def test_reaction_summary(self, sample_user):
        reaction = Reaction(sample_user, "like")
        summary = reaction.reaction_summary()
        assert summary["user"] == "testuser"
        assert summary["type"] == "like"


class TestBookmark:
    def test_bookmark_creation(self):
        bookmark = Bookmark("user123", "post456")
        assert bookmark.user_id == "user123"
        assert bookmark.post_id == "post456"

    def test_add_tag(self):
        bookmark = Bookmark("user123", "post456")
        result = bookmark.add_tag("important")
        assert result["added"] == True
        assert result["tags_count"] == 1
        assert "important" in bookmark.tags

    def test_remove_tag_exists(self):
        bookmark = Bookmark("user123", "post456")
        bookmark.add_tag("important")
        result = bookmark.remove_tag("important")
        assert result["removed"] == True
        assert result["tags_count"] == 0

    def test_remove_tag_not_exists(self):
        bookmark = Bookmark("user123", "post456")
        result = bookmark.remove_tag("important")
        assert result["removed"] == False


class TestContentAnalytics:
    def test_content_analytics_creation(self):
        analytics = ContentAnalytics()
        assert analytics.views == 0
        assert analytics.likes == 0
        assert analytics.shares == 0

    def test_aggregate_engagement(self):
        analytics = ContentAnalytics(views=100, likes=10, shares=5, impressions=100)
        result = analytics.aggregate_engagement()
        assert result["engagement_rate"] == 0.15  # (10 + 5) / 100

    def test_aggregate_engagement_zero_impressions(self):
        analytics = ContentAnalytics(impressions=0)
        result = analytics.aggregate_engagement()
        assert result["engagement_rate"] == 0.0


# Tests for Communication Module
class TestMessage:
    def test_message_creation(self, sample_user):
        message = Message(sample_user, "Hello world!")
        assert message.sender == sample_user
        assert message.text == "Hello world!"
        assert message.edited == False

    def test_edit_message(self, sample_user):
        message = Message(sample_user, "Hello!")
        result = message.edit("Edited message")
        assert result["edited"] == True
        assert message.text == "Edited message"
        assert message.edited == True

    def test_mark_read(self, sample_user):
        message = Message(sample_user, "Hello!")
        result = message.mark_read("user123")
        assert result["added"] == True
        assert result["read_by_count"] == 1
        assert "user123" in message.read_by

    def test_mark_read_duplicate(self, sample_user):
        message = Message(sample_user, "Hello!")
        message.mark_read("user123")
        result = message.mark_read("user123")
        assert result["added"] == False


class TestChat:
    def test_chat_creation(self, sample_chat):
        assert sample_chat.topic == "Test Chat"
        assert sample_chat.is_group == False

    def test_add_participant(self, sample_chat, sample_user2):
        participant = ChatParticipant(sample_user2)
        result = sample_chat.add_participant(participant)
        assert result["added"] == True
        assert result["participants"] == 1
        assert len(sample_chat.participants) == 1

    def test_get_recent_history(self, sample_chat, sample_user):
        # Add multiple messages
        for i in range(15):
            message = Message(sample_user, f"Message {i}")
            sample_chat.append_message(message)

        recent = sample_chat.get_recent_history(10)
        assert len(recent) == 10


class TestChatParticipant:
    def test_chat_participant_creation(self, sample_user2):
        participant = ChatParticipant(sample_user2)
        assert participant.user == sample_user2
        assert participant.is_admin == False

    def test_promote_to_admin(self, sample_user2):
        participant = ChatParticipant(sample_user2)
        result = participant.promote_to_admin()
        assert result["promoted"] == True
        assert participant.is_admin == True

    def test_mute(self, sample_user2):
        participant = ChatParticipant(sample_user2)
        result = participant.mute(True)
        assert result["muted"] == True
        assert result["changed"] == True
        assert participant.muted == True


class TestNotification:
    def test_notification_creation(self):
        notification = Notification("user123", "Test notification")
        assert notification.user_id == "user123"
        assert notification.content == "Test notification"
        assert notification.read == False

    def test_send_notification(self):
        notification = Notification("user123", "Test notification")
        result = notification.send_notification()
        assert result["sent"] == True

    def test_mark_as_seen(self):
        notification = Notification("user123", "Test notification")
        result = notification.mark_as_seen()
        assert result["read"] == True
        assert notification.read == True

    def test_escalate_priority(self):
        notification = Notification("user123", "Test notification")
        result = notification.escalate_priority()
        assert result["priority"] == "high"
        assert result["changed"] == True
        assert notification.priority == "high"

    def test_escalate_priority_already_high(self):
        notification = Notification("user123", "Test notification")
        notification.priority = "high"
        result = notification.escalate_priority()
        assert result["changed"] == False


class TestAnnouncement:
    def test_announcement_creation(self):
        announcement = Announcement("Title", "Body content")
        assert announcement.title == "Title"
        assert announcement.body == "Body content"
        assert announcement.published == False

    def test_publish(self):
        announcement = Announcement("Title", "Body content")
        result = announcement.publish()
        assert result["published"] == True
        assert announcement.published == True

    def test_revoke(self):
        announcement = Announcement("Title", "Body content")
        announcement.publish()
        result = announcement.revoke()
        assert result["revoked"] == True
        assert announcement.published == False


# Tests for Groups Module
class TestGroup:
    def test_group_creation(self, sample_group, sample_user):
        assert sample_group.name == "Test Group"
        assert sample_group.description == "Test Description"
        assert sample_group.owner == sample_user

    def test_add_member(self, sample_group, sample_user2):
        member = GroupMember(sample_user2)
        result = sample_group.add_member(member)
        assert result["added"] == True
        assert result["members"] == 1
        assert len(sample_group.members) == 1

    def test_remove_member(self, sample_group, sample_user2):
        member = GroupMember(sample_user2)
        sample_group.add_member(member)
        result = sample_group.remove_member(member)
        assert result["removed"] == True
        assert result["members"] == 0

    def test_member_count(self, sample_group, sample_user2):
        member = GroupMember(sample_user2)
        sample_group.add_member(member)
        assert sample_group.member_count() == 1


class TestGroupMember:
    def test_group_member_creation(self, sample_user2):
        member = GroupMember(sample_user2)
        assert member.user == sample_user2
        assert member.role == "member"

    def test_promote_to_admin(self, sample_user2):
        member = GroupMember(sample_user2)
        result = member.promote_to_admin()
        assert result["promoted"] == True
        assert member.role == "admin"

    def test_deactivate_membership(self, sample_user2):
        member = GroupMember(sample_user2)
        result = member.deactivate_membership()
        assert result["active"] == False
        assert result["changed"] == True
        assert member.active == False


class TestGroupSettings:
    def test_group_settings_creation(self):
        settings = GroupSettings()
        assert settings.privacy == "public"
        assert settings.post_moderation == False

    def test_set_privacy_valid(self):
        settings = GroupSettings()
        result = settings.set_privacy("private")
        assert result["privacy"] == "private"
        assert result["updated"] == True
        assert settings.privacy == "private"

    def test_set_privacy_invalid(self):
        settings = GroupSettings()
        original_privacy = settings.privacy
        result = settings.set_privacy("invalid")
        assert result["updated"] == False
        assert settings.privacy == original_privacy


class TestGroupInvitation:
    def test_group_invitation_creation(self, sample_user, sample_user2):
        invitation = GroupInvitation("group123", sample_user2, sample_user)
        assert invitation.group_id == "group123"
        assert invitation.invitee == sample_user2
        assert invitation.inviter == sample_user

    def test_send_invitation(self, sample_user, sample_user2):
        invitation = GroupInvitation("group123", sample_user2, sample_user)
        result = invitation.send_invitation()
        assert result["sent"] == True
        assert result["status"] == "sent"

    def test_accept_invitation(self, sample_user, sample_user2):
        invitation = GroupInvitation("group123", sample_user2, sample_user)
        result = invitation.accept_invitation()
        assert result["accepted"] == True
        assert result["status"] == "accepted"

    def test_decline_invitation(self, sample_user, sample_user2):
        invitation = GroupInvitation("group123", sample_user2, sample_user)
        result = invitation.decline_invitation()
        assert result["declined"] == True
        assert result["status"] == "declined"


# Tests for Events Module
class TestEvent:
    def test_event_creation(self, sample_event, sample_user):
        assert sample_event.title == "Test Event"
        assert sample_event.host == sample_user
        assert sample_event.location == "Test Location"

    def test_add_attendee(self, sample_event, sample_user2):
        attendee = EventAttendee(sample_user2)
        result = sample_event.add_attendee(attendee)
        assert result["added"] == True
        assert result["attendees"] == 1
        assert len(sample_event.attendees) == 1

    def test_cancel_event(self, sample_event):
        result = sample_event.cancel_event()
        assert result["canceled"] == True
        assert sample_event.canceled == True

    def test_event_summary(self, sample_event, sample_user):
        summary = sample_event.event_summary()
        assert summary["title"] == "Test Event"
        assert summary["host"] == "testuser"
        assert summary["attendees"] == 0


class TestEventAttendee:
    def test_event_attendee_creation(self, sample_user2):
        attendee = EventAttendee(sample_user2)
        assert attendee.user == sample_user2
        assert attendee.status == "going"

    def test_register_attendee(self, sample_user2):
        attendee = EventAttendee(sample_user2, "pending")
        result = attendee.register_attendee()
        assert result["status"] == "going"
        assert attendee.status == "going"

    def test_remove_attendee(self, sample_user2):
        attendee = EventAttendee(sample_user2)
        result = attendee.remove_attendee()
        assert result["status"] == "not_attending"
        assert attendee.status == "not_attending"

    def test_attendee_info(self, sample_user2):
        attendee = EventAttendee(sample_user2)
        info = attendee.attendee_info()
        assert info["user"] == "frienduser"
        assert info["status"] == "going"


class TestEventReminder:
    def test_event_reminder_creation(self):
        reminder = EventReminder("event123", "2023-01-01")
        assert reminder.event_id == "event123"
        assert reminder.remind_at == "2023-01-01"
        assert reminder.sent == False

    def test_schedule_reminder(self):
        reminder = EventReminder("event123", "2023-01-01")
        result = reminder.schedule_reminder()
        assert result["scheduled"] == True

    def test_cancel_reminder(self):
        reminder = EventReminder("event123", "2023-01-01")
        result = reminder.cancel_reminder()
        assert result["canceled"] == True
        assert reminder.sent == False


# Tests for System Module
class TestFeed:
    def test_feed_creation(self):
        feed = Feed("user123")
        assert feed.owner_id == "user123"
        assert feed.posts == []

    def test_generate_feed(self, sample_user):
        posts = [
            Post(sample_user, "Post 1", likes=10),
            Post(sample_user, "Post 2", likes=5),
            Post(sample_user, "Post 3", likes=15)
        ]
        feed = Feed("user123", posts)
        ranked = feed.generate_feed()
        assert len(ranked) == 3


class TestFeedAlgorithm:
    def test_feed_algorithm_creation(self):
        algorithm = FeedAlgorithm()
        assert algorithm.weight_recent == 1.0
        assert algorithm.weight_popularity == 1.0

    def test_calculate_relevance_score(self, sample_post):
        algorithm = FeedAlgorithm()
        sample_post.likes = 10
        score = algorithm.calculate_relevance_score(sample_post)
        assert score > 0

    def test_sort_by_priority(self, sample_user):
        posts = [
            Post(sample_user, "Post 1", likes=10),
            Post(sample_user, "Post 2", likes=5),
            Post(sample_user, "Post 3", likes=15)
        ]
        algorithm = FeedAlgorithm()
        ranked = algorithm.sort_by_priority(posts)
        assert ranked[0].likes >= ranked[1].likes


class TestSearch:
    def test_search_creation(self):
        search = Search()
        assert search.index is not None


    def test_index_item(self):
        search = Search()
        result = search.index_item("test item")
        assert result["indexed"] == True


class TestSearchIndex:
    def test_search_index_creation(self):
        index = SearchIndex()
        assert index.storage == []

    def test_clear_index(self):
        index = SearchIndex()
        index.method_1("test item")
        result = index.clear_index()
        assert result == True
        assert len(index.storage) == 0


class TestAnalytics:
    def test_analytics_creation(self):
        analytics = Analytics()
        assert analytics.metrics == {}

    def test_top_metrics(self):
        analytics = Analytics()
        analytics.record_metric("logins", 10)
        analytics.record_metric("posts", 5)
        analytics.record_metric("likes", 15)

        top = analytics.top_metrics(2)
        assert len(top) == 2
        assert top[0][1] >= top[1][1]  # sorted descending


class TestModeration:
    def test_moderation_creation(self):
        moderation = Moderation(["spam", "offensive"])
        assert len(moderation.rules) == 2

    def test_check_content_allowed(self):
        moderation = Moderation(["spam", "offensive"])
        allowed = moderation.check_content("This is good content")
        assert allowed == True

    def test_check_content_blocked(self):
        moderation = Moderation(["spam", "offensive"])
        allowed = moderation.check_content("This is spam content")
        assert allowed == False

class TestContentModeration:
    def test_content_moderation_creation(self):
        cm = ContentModeration()
        assert cm.queue == []

    def test_process_next_with_items(self):
        cm = ContentModeration()
        cm.add_to_queue("content1")
        result = cm.process_next()
        assert result == "content1"
        assert len(cm.queue) == 0

    def test_process_next_empty(self):
        cm = ContentModeration()
        result = cm.process_next()
        assert result is None


class TestUserModeration:
    def test_user_moderation_creation(self):
        um = UserModeration()
        assert um.flagged_users == []

    def test_flag_user(self):
        um = UserModeration()
        result = um.flag_user("user123")
        assert result["flagged"] == True
        assert result["count"] == 1
        assert "user123" in um.flagged_users

    def test_flag_duplicate_user(self):
        um = UserModeration()
        um.flag_user("user123")
        result = um.flag_user("user123")
        assert result["flagged"] == False

    def test_list_flagged(self):
        um = UserModeration()
        um.flag_user("user123")
        um.flag_user("user456")
        flagged = um.list_flagged()
        assert len(flagged) == 2


class TestBackup:
    def test_backup_creation(self):
        backup = Backup()
        assert backup.last_backup is None
        assert backup.history == []

class TestReport:
    def test_report_creation(self):
        report = Report("Test Report", "Content here")
        assert report.title == "Test Report"
        assert report.content == "Content here"

    def test_generate_summary(self):
        report = Report("Test Report", "Content here")
        summary = report.generate_summary()
        assert summary["title"] == "Test Report"
        assert summary["length"] == 12

    def test_export_pdf(self):
        report = Report("Test Report", "Content")
        result = report.export_pdf()
        assert result["exported"] == True


# Tests for Business Module
class TestAdvertisement:
    def test_advertisement_creation(self):
        ad = Advertisement("Test Advertiser", "Ad content", 1000)
        assert ad.advertiser == "Test Advertiser"
        assert ad.content == "Ad content"
        assert ad.budget == 1000


    def test_consume_budget_exceed(self):
        ad = Advertisement("Test Advertiser", "Ad content", 50)
        result = ad.consume_budget(100)
        assert result["budget"] == 0

    def test_pause_ad(self):
        ad = Advertisement("Test Advertiser", "Ad content", 1000)
        result = ad.pause_ad()
        assert result["active"] == False
        assert ad.active == False


class TestSubscription:
    def test_subscription_creation(self):
        subscription = Subscription("user123", "free")
        assert subscription.user_id == "user123"
        assert subscription.plan == "free"
        assert subscription.active == True

    def test_cancel(self):
        subscription = Subscription("user123", "free")
        result = subscription.cancel()
        assert result["active"] == False
        assert subscription.active == False

    def test_upgrade_to_premium(self):
        subscription = Subscription("user123", "free")
        result = subscription.upgrade_to_premium()
        assert result["upgraded"] == True
        assert result["plan"] == "premium"
        assert subscription.plan == "premium"

    def test_upgrade_already_premium(self):
        subscription = Subscription("user123", "premium")
        result = subscription.upgrade_to_premium()
        assert result["upgraded"] == False


class TestPayment:
    def test_payment_creation(self):
        payment = Payment(100.0, "USD")
        assert payment.amount == 100.0
        assert payment.currency == "USD"
        assert payment.status == "pending"


    def test_refund(self):
        payment = Payment(100.0, "USD")
        payment.process_payment()
        result = payment.refund()
        assert result["status"] == "refunded"
        assert payment.status == "refunded"


class TestPremiumFeature:
    def test_premium_feature_creation(self):
        feature = PremiumFeature("Advanced Analytics")
        assert feature.name == "Advanced Analytics"
        assert feature.enabled == False

    def test_enable(self):
        feature = PremiumFeature("Advanced Analytics")
        result = feature.enable()
        assert result["enabled"] == True
        assert feature.enabled == True


class TestBusinessPage:
    def test_business_page_creation(self, sample_user):
        page = BusinessPage(sample_user, "Business info")
        assert page.owner == sample_user
        assert page.info == "Business info"
        assert page.followers == 0


class TestAiRecommendation:
    def test_ai_recommendation_creation(self):
        ai = AiRecommendation("simple_model")
        assert ai.model_name == "simple_model"

    def test_recommend(self, sample_user):
        posts = [
            Post(sample_user, "Post 1", likes=10),
            Post(sample_user, "Post 2", likes=5)
        ]
        ai = AiRecommendation()
        recommendations = ai.recommend(posts)
        assert len(recommendations) == 2

    def test_model_info(self):
        ai = AiRecommendation("test_model")
        info = ai.model_info()
        assert info["model"] == "test_model"


class TestMetrics:
    def test_metrics_creation(self):
        metrics = Metrics()
        assert metrics.analytics is not None


    def test_top(self):
        metrics = Metrics()
        metrics.record("engagement", 10)
        metrics.record("posts", 5)
        top = metrics.top(2)
        assert len(top) == 2


class TestScheduler:
    def test_scheduler_creation(self):
        scheduler = Scheduler()
        assert scheduler.tasks == []


    def test_pop_next_task_with_tasks(self):
        scheduler = Scheduler()
        reminder = EventReminder("event123")
        scheduler.schedule_reminder(reminder)
        task = scheduler.pop_next_task()
        assert task is not None

    def test_pop_next_task_empty(self):
        scheduler = Scheduler()
        task = scheduler.pop_next_task()
        assert task is None


class TestIntegration:
    def test_integration_creation(self):
        integration = Integration("ServiceX")
        assert integration.provider == "ServiceX"
        assert integration.enabled == False

    def test_enable_integration(self):
        integration = Integration("ServiceX")
        result = integration.enable_integration()
        assert result["enabled"] == True
        assert integration.enabled == True

    def test_update_config(self):
        integration = Integration("ServiceX")
        result = integration.update_config({"key": "value"})
        assert result["applied"] == True
        assert integration.config["key"] == "value"

    def test_update_config_invalid(self):
        integration = Integration("ServiceX")
        result = integration.update_config("invalid")
        assert result["applied"] == False


# Tests for Exceptions
class TestExceptions:
    def test_user_not_found_exception(self):
        with pytest.raises(UserNotFound):
            raise UserNotFound("User not found")

    def test_user_exists_exception(self):
        with pytest.raises(UserExists):
            raise UserExists("User already exists")

    def test_invalid_credentials_exception(self):
        with pytest.raises(InvalidCredentials):
            raise InvalidCredentials("Invalid credentials")

    def test_post_not_found_exception(self):
        with pytest.raises(PostNotFound):
            raise PostNotFound("Post not found")

    def test_post_access_denied_exception(self):
        with pytest.raises(PostAccessDenied):
            raise PostAccessDenied("Access denied")

# Integration Tests
class TestIntegrationScenarios:
    def test_complete_user_workflow(self, sample_user, sample_user2):
        # User registration and authentication
        registration = sample_user.register()
        assert registration["status"] == "registered"

        auth_result = sample_user.authenticate("password123")
        assert auth_result["authenticated"] == True

        # Profile management
        sample_user.profile.update_bio("Integration test bio")
        assert sample_user.profile.bio == "Integration test bio"

        # Friend request
        friend_request = FriendRequest(sample_user, sample_user2, "Hello!")
        send_result = friend_request.send_request()
        assert send_result["status"] == "sent"

        accept_result = friend_request.accept_request()
        assert accept_result["accepted"] == True

    def test_content_creation_workflow(self, sample_user):
        # Create post
        post = Post(sample_user, "Integration test post")
        assert post.text == "Integration test post"

        # Add media
        media = Media("http://example.com/image.jpg")
        media_result = post.attach_media(media)
        assert media_result["added"] == True

        # Add comment
        comment = Comment(sample_user, "Nice post!")
        comment_result = post.add_comment(comment)
        assert comment_result["succeeded"] == True

        # Add like
        like = Like(sample_user)
        like_result = like.add_like()
        assert like_result["liked"] == True
