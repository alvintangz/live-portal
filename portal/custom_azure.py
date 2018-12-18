from storages.backends.azure_storage import AzureStorage
import os

class AzureMediaStorage(AzureStorage):
    account_name = 'liveportal2019' # Must be replaced by your <storage_account_name>
    account_key = os.environ.get('LP_AZURE_STORAGE_KEY', '') # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'liveportal2019' # Must be replaced by your storage_account_name
    account_key = os.environ.get('LP_AZURE_STORAGE_KEY', '') # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None