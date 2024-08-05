import os
import tarfile

def get_package_names_from_db(db_file):        
    sync_db_path = '/var/lib/pacman/sync'  # Path to the sync database

    db_files = [os.path.join(sync_db_path, f) for f in os.listdir(sync_db_path) if f.endswith('.db')]
    all_package_names = []
    for db_file in db_files:
        package_names = []

        with tarfile.open(db_file, 'r:*') as tar:
            for member in tar.getmembers():
                if member.isdir():
                    package_names.append(member.name)
        all_package_names.extend(package_names)
    return all_package_names

