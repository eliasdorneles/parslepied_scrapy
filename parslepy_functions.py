import re

import parslepy


def duration(user_ctx, xpath_ctx, attributes, *args):
    """Parses a duration time as per Youtube API, and
    returns a human readable string

    >>> duration(None, None, ['PT2M47S'])
    '00:02:47'
    """
    pattern = '^PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'

    # expecting the string will come in attributes looks a bit funny to me,
    # because the function looks too tight to the parselet expression (eg: what
    # if I update the parselet to get an element body instead of an attribute?)
    if attributes:
        time_str = attributes[0]
        match = re.match(pattern, time_str)

        if match:
            hours, minutes, seconds = match.groups()
            return '%02d:%02d:%02d' % (
                int(hours or 0), int(minutes or 0), int(seconds))
    return ''


selector_handler = parslepy.DefaultSelectorHandler(
    namespaces={'user': 'local-extensions'},
    extensions={
        ('local-extensions', 'duration'): duration,
    })
