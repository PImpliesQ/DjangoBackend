from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.conf import settings
from clerk import Client as ClerkClient
from django.contrib.auth import get_user_model
from .models import CustomUser  # Import CustomUser model

def clerk_callback(request):
    clerk_client = ClerkClient()
    session_token = request.GET.get('token')
    clerk_user = clerk_client.users.verify_session_token(session_token)

    
    user = sync_user_with_clerk(clerk_user)

    
    if user.role == CustomUser.UserRole.PLAYER:
        return redirect('/player_dashboard/')
    elif user.role == CustomUser.UserRole.GAME_KEEPER:
        return redirect('/game_keeper_dashboard/')
    
    # Default redirection if the role is not recognized or not logged in
    return redirect('/')


def sync_user_with_clerk(clerk_user):
    User = get_user_model()
    try:
        user = User.objects.get(email=clerk_user['email'])
    except User.DoesNotExist:
        user = User.objects.create(
            username=clerk_user['username'],
            email=clerk_user['email'],
            role=...  
        )
    return user
