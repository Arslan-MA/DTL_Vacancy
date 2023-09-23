from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VacancyTitle(models.Model):
    title = models.CharField(max_length=255,
                             unique=True)

    def __str__(self):
        return self.title


class Requirement(models.Model):
    requirement = models.CharField(max_length=255)

    def __str__(self):
        return self.requirement


class Job(models.Model):
    v_title = models.ForeignKey(VacancyTitle, null=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    requirements = models.ManyToManyField(Requirement)
    salary = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.company} - {self.v_title} - {self.salary}"

    def get_absolute_url(self):
        return f"vacancy_detail/{self.pk}"
