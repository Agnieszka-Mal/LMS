from django.contrib.auth.mixins import AccessMixin


class OwnerRquiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        #('*' * 20)
        #print(args)
        #print(kwargs)
        #print('*' * 20)
        course = self.get_queryset().get(pk=kwargs.get('pk'))
        if request.user != course.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)



