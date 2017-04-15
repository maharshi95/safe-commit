# Author: Maharshi Gor

class JobStatus:
    CREATED = 'Created'
    IN_PROGRESS = 'In Progress'
    FAILED = 'Failed'
    COMPLETE = 'Complete'

    @classmethod
    def values(cls):
        return (cls.CREATED, cls.IN_PROGRESS, cls.FAILED, cls.COMPLETE)

    @classmethod
    def choices(cls):
        return tuple([(v,v) for v in cls.values()])