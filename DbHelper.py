connect_str = "DRIVER={ODBC Driver 17 for SQL Server};" \
                    "SERVER=DESKTOP-J65EBGL;" \
                    "DATABASE=video_processing;" \
                    "UID=sa;" \
                    "PWD=111"


def create_video_seg(connection, segments):
    try:
        command = "exec create_segments '{0}'".format(segments)
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Exception as e:
        print(e)


def create_frame_seq(connection, sequences):
    try:
        command = "exec create_sequences '{0}'".format(sequences)
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Exception as e:
        print(e)


def create_frame(connection, frames):
    try:
        command = "exec create_frames '{0}'".format(frames)
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Exception as e:
        print(e)


def create_person(connection, people):
    try:
        command = "exec create_people '{0}'".format(people)
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Exception as e:
        print(e)


def create_things(connection, things):
    try:
        command = "exec create_thing '{0}'".format(things)
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except Exception as e:
        print(e)

def ex_query(connection, command):
    try:
        result = list()
        print(command)
        cursor = connection.cursor()
        cursor.execute(command)
        for row in cursor.fetchall():
            result.append({
                'id': row.FrameID,
                'frame_seq_id': row.FrameSegID,
                'frame': row.FrameContent
            })
        return result
    except Exception as e:
        print(e)
