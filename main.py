import logging

import handler
import logsetup


def main():
    logger.info("Main executed")

    handler.SafeLoaderPlusTuples.add_constructor(u'tag:yaml.org,2002:/python/tuple',
                                         handler.SafeLoaderPlusTuples.construct_tuple)

    handler_ = handler.Handler()
    handler_.run()
    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, handlers=[])
    logger = logsetup.setup_log(__name__)
    main()
else:
    raise ImportError("This file is not supposed to be imported as a module")
