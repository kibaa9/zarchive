from django.db.models import Sum, Avg


class AnnotateBookMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.annotate(
            total_rating=Sum('reviews__rating'),
            average_rating=Avg('reviews__rating')
        )
