from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin):
    """Base mixin for class-based views in the project.

    Inherit from this alongside Django's generic views to keep
    authentication and other project-wide view defaults consistent.
    """
