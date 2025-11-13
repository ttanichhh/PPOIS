User 9 5 -> Profile, UserPreferences, UserStatistics        
Profile 6 3 -> PrivacySettings      
PrivacySettings 4 3     
UserPreferences 4 3     
UserStatistics 5 3      
FriendRequest 6 3       
UserAnalytics 2 3       

Post 8 3 -> User, Comment, Media        
Comment 5 2 -> User         
Like 5 3 -> User        
Media 5 2       
Hashtag 4 2         
Poll 4 3 -> PollOption      
PollOption 3 2      
Story 5 2 -> StoryViewer        
StoryViewer 3 2     
Reaction 4 2        
Bookmark 4 2        
ContentAnalytics 5 2        
    
Message 5 3 -> User, Chat       
Chat 5 3 -> ChatParticipant, Message        
ChatParticipant 4 2 -> User     
Notification 5 3        
Announcement 5 2        

Group 6 3 -> User, GroupMember      
GroupMember 4 2 -> User     
GroupSettings 4 2       
GroupInvitation 5 3 -> User         

Event 6 3 -> User, EventAttendee        
EventAttendee 4 3 -> User       
EventReminder 4 2       

Feed 4 2 -> Post, FeedAlgorithm     
FeedAlgorithm 2 2       
Search 2 2 -> SearchIndex       
SearchIndex 2 3     
Analytics 2 2 -> SearchIndex        
Moderation 3 2 -> ContentAnalytics      
ContentModeration 1 2       
UserModeration 1 2      
Backup 2 2      
Report 3 2      

Advertisement 5 2   
Subscription 5 2        
Payment 5 2     
PremiumFeature 4 2      
BusinessPage 5 2        
AiRecommendation 3 2 -> FeedAlgorithm       
Metrics 3 2 -> Analytics        
Scheduler 2 2 -> EventReminder      
Integration 4 2   

Exceptions(12):  
EventNotFound 0 0 ->        
EventRegistrationError 0 0 ->        
GroupNotFound 0 0 ->        
GroupPermission 0 0 ->        
MediaUploadError 0 0 ->        
MessageNotFound 0 0 ->        
PostAccessDenied 0 0 ->        
PostNotFound 0 0 ->        
UserExists 0 0 ->        
UserNotFound 0 0 ->        

Классов: 50     
Полей: 206      
Методов: 120        
Ассоциаций: 31      
Исключения: 12  

