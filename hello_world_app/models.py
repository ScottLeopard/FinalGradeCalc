from django.db import models

class GradeEntry(models.Model):
    course_name = models.CharField(max_length=100)
    current_grade = models.FloatField()       # current grade as a percent
    desired_grade = models.FloatField()       # desired final grade as a percent
    final_weight = models.FloatField()        # weight of the final exam as a percent

    @property
    def required_score(self):
        """
        Formula: desired = current*(1 - final_weight/100) + score*(final_weight/100)
        Solve for score:
        score = (desired - current*(1 - final_weight/100)) / (final_weight/100)
        """
        w = self.final_weight / 100.0
        if w == 0:
            return None
        score = (self.desired_grade - self.current_grade * (1 - w)) / w
        return round(score, 2)

    def __str__(self):
        return f'{self.course_name}'
