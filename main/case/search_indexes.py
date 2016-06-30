from haystack import indexes
from .models import Content
class PostIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	#doctor = indexes.CharField(model_attr='doctor')
	#name = indexes.CharField(model_attr='name')
	def get_model(self):
		return Content
	def index_queryset(self, using=None):
		return self.get_model().objects.all()
