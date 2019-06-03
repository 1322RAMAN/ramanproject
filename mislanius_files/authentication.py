def authentication(auth,email,dmail):
    try:
        if auth==True:
            if email==dmail:
                return True
            else:
                return False,"Wrong User"
        else:
            return False,"not Login"
    except:
        return False,"Not Login"