from db.life_log_1 import LifeLog1
import request_getter
import response_generator
from debug import logger


def main(event, context):

    logger.info('start main')
    res = response_generator.Response()

    try:
        input_data = request_getter.Request(event=event, context=context)
        kind, val = input_data.get()
    except KeyError as e:
        logger.error('err request parse >> %s', str(e))
        return res.generate_fail(detail=str(e))

    logger.info('kind:%d, val:%f', kind, val)

    logger.info('start database')
    try:
        table = LifeLog1()
        table.insert(kind=kind, val=val)
        result = table.check_records()
        logger.debug(result)
    except Exception as e:
        logger.error('err database >> %s', str(e))
        return res.generate_fail(detail=str(e))
    logger.info('end database')

    logger.info('end main')
    return res.generate_success()


def lambda_handler(event, context):
    return main(event=event, context=context)
