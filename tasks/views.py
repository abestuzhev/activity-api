import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from categories.models import Category
from helpers.functions import format_date
from tasks.models import Task
from tasks.serialazers import TaskDetailSerialazer, TaskListSerialazer, TaskCreateSerialazer


def hello(request):
    return HttpResponse("Hello world")


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerialazer
    # permission_classes = [IsAuthenticated]


class TaskDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerialazer


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerialazer


@method_decorator(csrf_exempt, name="dispatch")
class TaskUpdateView(UpdateView):
    model = Task
    fields = ["title", "text", "status", "start", "end"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        task_data = json.loads(request.body)

        self.object.title = task_data["title"]
        self.object.created = task_data["created"]
        self.object.text = task_data["text"]
        self.object.status = task_data["status"]
        self.object.isImportant = task_data["isImportant"]
        self.object.start = format_date(task_data["start"])
        self.object.end = format_date(task_data["end"])

        for category in task_data["categories"]:
            try:
                category_obg = Category.objects.get(id=category);
            except Category.DoesNotExist:
                return JsonResponse({'error', 'Category not found'}, status=404)
            self.object.categories.add(category_obg)

        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "categories": list(self.object.categories.all().values_list("id", flat=True)),
            "title": self.object.title,
            "text": self.object.text,
            "status": self.object.status,
            "isImportant": self.object.isImportant,
            "created": self.object.created,
            "start": self.object.start,
            "end": self.object.end,
            "user": self.object.user_id,
        })


@method_decorator(csrf_exempt, name="dispatch")
class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

# Реализация класса без REST-framework

# Реализация класса без REST-framework
# class TaskListView(ListView):
#     model = Task
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         search_text = request.GET.get("q", None)
#         if search_text:
#             self.object_list = self.object_list.filter(title=search_text)
#
#         self.object_list = self.object_list.order_by("id")
#
#         response = []
#         for task in self.object_list:
#             response.append({
#                 "id": task.id,
#                 "title": task.title,
#                 "text": task.text,
#                 "status": task.status,
#                 "created": task.created,
#                 "start": format_date(task.start),
#                 "end": format_date(task.end),
#             })
#         return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


# class TaskDetailView(DetailView):
#     model = Task
#
#     def get(self, request, *args, **kwargs):
#         task = self.get_object()
#
#         return JsonResponse(TaskDetailSerialazer(task).date)


# @method_decorator(csrf_exempt, name="dispatch")
# class TaskCreateView(CreateView):
#     model = Task
#     fields = ["user", "title", "text", "status", "created", "start", "end"]
#
#     def post(self, request, *args, **kwargs):
#         task_data = json.loads(request.body)
#         task = Task.objects.create(
#             user_id=task_data["user_id"],
#             title=task_data["title"],
#             text=task_data["text"],
#             status=task_data["status"],
#             start=format_date(task_data["start"]),
#             end=format_date(task_data["end"]),
#         )
#
#         return JsonResponse({
#             "id": task.id,
#             "title": task.title,
#             "text": task.text,
#             "status": task.status,
#             "start": task.start,
#             "end": task.end,
#             "task_data": task_data
#         })
