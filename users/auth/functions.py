
def is_delegate(request):
    return request.user.is_delegate and hasattr(request.user, 'delegate')
    
def is_partner(request):
    return request.user.is_partner and hasattr(request.user, 'partner')
    
def is_judge(request):
    return request.user.is_judge and hasattr(request.user, 'judge')