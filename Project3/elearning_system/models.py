from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=50, )
    password = models.CharField(max_length=30, )
    user_name = models.CharField(max_length=30, )
    email_address = models.CharField(max_length=50, )
    block_status = models.CharField(max_length=10, )
    contribute_number = models.IntegerField(default=0)
    solve_number = models.IntegerField(default=0)

    def __repr__(self):
        return self.user_name


class Role(models.Model):
    role_name = models.CharField(max_length=30, )
    user_list = models.ManyToManyField(User)

    def __repr__(self):
        return self.role_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50, )

    def __str__(self):
        return self.tag_name


class ExerciseWebServer(models.Model):

    view_number = models.IntegerField(default=0)
    solve_number = models.IntegerField(default=0)
    contributor = models.ForeignKey(User, null=False, related_name='contributor')
    approver = models.ForeignKey(User, null=True, related_name='approver',on_delete=models.SET_NULL)
    date_created = models.DateTimeField()
    tag = models.ForeignKey(Tag, null=True,on_delete=models.SET_NULL)
    user_list = models.ManyToManyField(User)

    def __str__(self):
        return self.id


class ErrorMessage(models.Model):
    title = models.CharField(max_length=30, )
    content = models.CharField(max_length=255, )
    reporter = models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    exercise_report = models.ForeignKey(ExerciseWebServer,
                                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title
