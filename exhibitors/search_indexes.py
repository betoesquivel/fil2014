from haystack import indexes
from exhibitors.models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    priority = indexes.IntegerField(model_attr='priority')

    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        #return self.get_model().objects.filter(priority__lte=datetime.datetime.now())
        return self.get_model().objects.all()
