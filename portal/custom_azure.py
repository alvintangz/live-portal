from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'liveportal2019' # Must be replaced by your <storage_account_name>
    account_key = 'PA4c7t/0sCEdPElAyz6TkyDXqOGWaCZnXd9kPu7GJ65leJXNZRuSZ2nM3zwN9UPcfs0aZbFpEJzAGwrDfEz99w==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'liveportal2019' # Must be replaced by your storage_account_name
    account_key = 'PA4c7t/0sCEdPElAyz6TkyDXqOGWaCZnXd9kPu7GJ65leJXNZRuSZ2nM3zwN9UPcfs0aZbFpEJzAGwrDfEz99w==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None