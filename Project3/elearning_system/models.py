from __future__ import unicode_literals

from django.db import models


# Create your model here.

class User(models.Model):
    account_name = models.CharField(max_length=20,)
    password = models.CharField(max_length=30,)
    user_name = models.CharField(max_length=30,)
    email_address = models.CharField(max_length=30,)
    block_status = models.CharField(max_length=10,)
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
    tag_name = models.CharField(max_length=30, )

    def __str__(self):
        return self.tag_name

class ExerciseWebServer(models.Model):
    view_number = models.IntegerField()
    solve_number = models.IntegerField()
    contributer_id = models.ForeignKey(User,null=True, related_name='user_contributer')
    approver_id = models.ForeignKey(User,null=True, related_name='user_approver')
    created_date = models.DateTimeField()
    tag_id = models.ForeignKey(Tag,
                               on_delete=models.CASCADE)
    user_list = models.ManyToManyField(User)

    def __str__(self):
        return self.exercise_name

class ErrorMessage(models.Model):
    title = models.CharField(max_length=30, )
    content = models.CharField(max_length=255, )
    reporter_id = models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    reported_exercise_id = models.ForeignKey(ExerciseWebServer,
                                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

