from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    account_name = models.CharField(max_length=20, )
    password = models.CharField(max_length=30, )
    user_name = models.CharField(max_length=30, )
    email_address = models.CharField(max_length=30, )
    block_status = models.CharField(max_length=10, )

    def __repr__(self):
        return self.user_name


class Role(models.Model):
    role_name = models.CharField(max_length=30, )

    def __repr__(self):
        return self.role_name


class ErrorMessage(models.Model):
    title = models.CharField(max_length=30, )
    content = models.CharField(max_length=255, )
    reporter_id = models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    reported_exercise_id = models.ForeignKey(ExerciseWebServer,
                                             on_delete=models.CASCADE)

    def __repr__(self):
        return self.title


class ExerciseWebServer(models.Model):
    exercise_name = models.CharField(max_length=30, )
    view_number = models.IntegerField()
    solve_number = models.IntegerField()
    contributer_id = models.IntegerField()
    approver_id = models.IntegerField()
    created_date = models.DateTimeField()
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __repr__(self):
        return self.name


class Tag(models.Model):
    tag_name = models.CharField(max_length=30, )

    def __repr__(self):
        return self.tag_name


class UserSolveExercise(models.Model):
    exercise_id = models.ForeignKey(ExerciseWebServer, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __repr__(self):
        return self.user_id.user_name + ' : ' + self.exercise_id.exercise_name


class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __repr__(self):
        return self.user_id.user_name + ' is ' + self.role_id.role_name
