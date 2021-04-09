# def notification_context(request):
    
#     from notifications.signals import notify
#     from django.contrib.auth.models import User
#     if request.user.is_anonymous:
#         return {}
#     else:
#         user = User.objects.get(user__pk=request.user.pk) 

#         notify.send(request.user, recipient=user, actor=request.user,verb='followed you.', nf_type='followed_by_one_user')

#         return True
#     # Most of the code below is simply copied from the question, it
#     # would be different for different applications.  The important thing
#     # is that we have to figure out the values to be placed in the template
#     # context.

#     # If the user is not logged in, we don't know who they are so we return an empty.
#     # dictionary which results in nothing new being added to the template context.

#     # look up the notifications for the current user

# # your example view
        