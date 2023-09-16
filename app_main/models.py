from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator

# Create your models here.

class InfoModel(models.Model):
    name = models.CharField(max_length=122, null=True, verbose_name="Full Name")
    Image = models.ImageField(upload_to="profile", null=True, blank=True, verbose_name="Profile Picture")
    details = RichTextUploadingField(null=True, verbose_name="Short Summary")
    email = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=122, null=True, blank=True)

    link_git = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Github Link")
    link_li = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Linkedin Link")
    link_fb = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Facebook Link")
    link_scholar = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Google Scholar Link")
    resume = models.FileField(null=True, blank=True, upload_to="Resume-files", verbose_name="Resume", validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Informations"
        ordering = ["-id"]




class SkillsQualificationsModel(models.Model):
    field = models.CharField(max_length=555, null=True, verbose_name="Add Field")

    def __str__(self):
        return f"{self.field}"

    class Meta:
        verbose_name = "Skill & Qualification"
        verbose_name_plural = "Skills & Qualifications"
        ordering = ["-id"]




class TechStackModel(models.Model):
    field = models.CharField(max_length=555, null=True, verbose_name="Add Field")

    def __str__(self):
        return f"{self.field}"

    class Meta:
        verbose_name = "Tech Stack"
        verbose_name_plural = "Tech Stacks"
        ordering = ["-id"]




class EducationsModel(models.Model):
    field = models.CharField(max_length=555, null=True, verbose_name="Add Field")

    def __str__(self):
        return f"{self.field}"

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
        ordering = ["-id"]




class WorksModel(models.Model):
    designation = models.CharField(max_length=155, null=True)

    company = models.CharField(max_length=155, null=True, verbose_name="Company Name")
    link = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Company Link")

    job_start_date = models.DateField(default=timezone.now)
    job_end_date = models.DateField(null=True, blank=True)

    details = RichTextUploadingField(null=True, verbose_name="Job Summary")

    def __str__(self):
        return f"{self.designation}"

    class Meta:
        verbose_name = "Work History"
        verbose_name_plural = "Works History"
        ordering = ["-id"]




class ProjectsModel(models.Model):
    title = models.CharField(max_length=555, null=True, verbose_name="Project Title")
    link_git = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Github Link")
    link_live = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Live Link")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Project & Accomplishment"
        verbose_name_plural = "Projects & Accomplishments"
        ordering = ["-id"]



class PublicationModel(models.Model):
    title = models.CharField(max_length=555, null=True, verbose_name="Paper Title")
    link = models.URLField(null=True, blank=True, default="https://www.google.com/", verbose_name="Add Link")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Publication & Award"
        verbose_name_plural = "Publication & Awards"
        ordering = ["-id"]

