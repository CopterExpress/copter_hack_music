#!/usr/bin/env python

import os
import rospy
import requests
from download import download_url

from std_srvs.srv import Trigger, TriggerResponse
from copter_hack_music.srv import GetMusic, GetMusicResponse, PlayMusic, PlayMusicResponse


rospy.init_node('copter_hack_music')


BASE_URL = rospy.get_param('~server_url')
MUSIC_STORAGE = rospy.get_param('~storage')
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_music(req):
    try:
        filename = download_url(BASE_URL + '/get', os.path.expanduser(MUSIC_STORAGE), get_params=req.filename)
        return GetMusicResponse(success=True, filename=filename)
    except Exception as e:
        return GetMusicResponse(success=False, message=str(e))


def play(req):
    try:
        resp = requests.post(BASE_URL + '/play', data={'melody': req.filename, 'start': req.start})
        if resp.status_code != 200:
            return PlayMusicResponse(success=False, message=resp.text)
        return PlayMusicResponse(success=True)
    except Exception as e:
        return PlayMusicResponse(success=False, message=str(e))


def stop(req):
    try:
        resp = requests.post(BASE_URL + '/stop')
        if resp.status_code != 200:
            return TriggerResponse(success=False, message=resp.text)
        return TriggerResponse(success=True)
    except Exception as e:
        return TriggerResponse(success=False, message=str(e))


rospy.Service('~get', GetMusic, get_music)
rospy.Service('~play', PlayMusic, play)
rospy.Service('~stop', Trigger, stop)


rospy.spin()
