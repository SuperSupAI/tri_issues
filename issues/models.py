from django.db import models

# Create your models here.

class ISSUE(models.Model):
    STATUS = [
        ('open' , 'OPEN'),
        ('on going' , 'ON GOING'),
        ('closed' , 'CLOSED'),
    ]
    MACHINE_TYPE = [
        ('AOI', 'AOI'),
        ('AXI', 'AXI'),
        ('ICT', 'ICT'),
    ]
    PRIORITY = [
        ('HIGH','HIGH'),
        ('MEDIUM','MEDIUM'),
        ('LOW','LOW'),
        ('LOAN PART','LOAN PART'),
    ]
  
    issue = models.CharField(max_length=100)
    date = models.DateField()
    serial_no = models.CharField(max_length=15)
    customer = models.CharField(max_length=50)
    machine = models.CharField(max_length=3,choices=MACHINE_TYPE)
    model = models.CharField(max_length=50)
    problem = models.TextField()
    progress = models.TextField()
    executor = models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=STATUS, default='ON GOING')
    registered_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=15,null=True,blank=True,choices=PRIORITY,default='MEDIUM')

    def __str__(self) -> str:
        #return super().__str__()
        return '{}{}{}{}{}{}{}{}{}{}{}'.format (
            self.issue,
            self.date,
            self.customer,
            self.machine,
            self.model,
            self.problem,
            self.progress,
            self.executor,
            self.status,
            self.registered_at,
            self.priority,
            )
