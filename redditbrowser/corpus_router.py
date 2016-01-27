# noinspection PyMethodMayBeStatic
class CorpusRouter(object):
    """
    Routes all requests for reading corpus objects to the corpus database and ignores writes.
    """

    whitelist = ['comments_abridged', 'subreddits', 'subreddit_topics']

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to the corpus.
        :param model: the model in question
        """
        if model._meta.db_table in CorpusRouter.whitelist:
            return 'corpus'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to the corpus.
        :param model: the model in question
        """
        if model._meta.db_table in CorpusRouter.whitelist:
            return 'corpus'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model is from the corpus(?)
        :param obj1: first model instance in question
        :param obj2: second model instance in question
        """
        # if obj1._meta.app_label == 'auth' or \
        #    obj2._meta.app_label == 'auth':
        #    return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the corpus app only appears in the 'corpus'
        database.
        :param model: the model in question
        :param app_label: the application for which to perform this migration
        """
        # if app_label == 'interface':
        #     return db == 'auth_db'
        return None