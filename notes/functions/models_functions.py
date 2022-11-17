

def get_path_upload_record(instance, file):
    return f'records/user_{instance.user.id}/%Y/%m/%d/{file}'


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'

