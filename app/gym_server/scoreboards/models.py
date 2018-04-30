from django.db import models
from environments.models import Environment
from allauth.socialaccount.models import SocialAccount


class EvaluationRun(models.Model):
    user = models.ForeignKey(SocialAccount,
                             on_delete=models.CASCADE)
    env = models.ForeignKey(Environment, related_name='eval_runs',
                            on_delete=models.CASCADE)
    s3_path = models.CharField(max_length=255)
    high_score = models.FloatField()
    # what else?

    class Meta:
        verbose_name = 'Evaluation Run'
