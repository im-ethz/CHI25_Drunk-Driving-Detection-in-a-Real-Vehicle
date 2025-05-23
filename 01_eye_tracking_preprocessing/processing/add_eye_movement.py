#####################################################################
# Copyright (C) 2025 ETH Zürich (ethz.ch)
# Chair of Information Management (im.ethz.ch; github.com/im-ethz)
# Bosch Lab at University of St. Gallen and ETH Zürich (iot-lab.ch)
#
# Authors: Robin Deuber, Kevin Koch, Patrick Langer, Martin Maritsch
#
# Licensed under the MIT License (the "License");
# you may only use this file in compliance with the License.
# You may obtain a copy of the License at
#
#         https://mit-license.org/
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#####################################################################

import pandas as pd

def add_eye_movement(data: pd.DataFrame, data_eye: pd.DataFrame):
    """
    Adds the eye movement labels generated by remodnav to the data.
    """
    data_eye["start_time"] = pd.to_datetime(data_eye["start_time"])
    types = []
    event_peak_vel = []
    event_avg_vel = []
    event_med_vel = []
    event_amp_given = []
    event_duration = []
    
    current_type = data_eye["label"].iloc[0]
    current_peak_vel = data_eye["peak_vel"].iloc[0]
    current_avg_vel = data_eye["avg_vel"].iloc[0]
    current_med_vel = data_eye["med_vel"].iloc[0]
    current_amp_given = data_eye["amp"].iloc[0]
    current_duration = int((data_eye["end_time"].iloc[0] - 
                            data_eye["start_time"].iloc[0]).total_seconds() * 1000)
    
    index_eye_next = 1
    for i in range(len(data)):
        if index_eye_next < len(data_eye):
            if data.index[i] >= data_eye.index[index_eye_next]:
                current_type = data_eye["label"].iloc[index_eye_next]
                current_peak_vel = data_eye["peak_vel"].iloc[index_eye_next]
                current_avg_vel = data_eye["avg_vel"].iloc[index_eye_next]
                current_med_vel = data_eye["med_vel"].iloc[index_eye_next]
                current_amp_given = data_eye["amp"].iloc[index_eye_next]
                current_duration = int((data_eye["end_time"].iloc[index_eye_next] - 
                                        data_eye["start_time"].iloc[index_eye_next]).total_seconds() * 1000)
                index_eye_next = index_eye_next + 1
            types.append(current_type)
            event_peak_vel.append(current_peak_vel)
            event_avg_vel.append(current_avg_vel)
            event_med_vel.append(current_med_vel)
            event_amp_given.append(current_amp_given)
            event_duration.append(current_duration)
            
        elif index_eye_next == len(data_eye):
            types.append(current_type)
            event_peak_vel.append(current_peak_vel)
            event_avg_vel.append(current_avg_vel)
            event_med_vel.append(current_med_vel)
            event_amp_given.append(current_amp_given)
            event_duration.append(current_duration)

    data["eye_movement_type"] = types
    data["eye_movement_peak_vel"] = event_peak_vel
    data["eye_movement_avg_vel"] = event_avg_vel
    data["eye_movement_med_vel"] = event_med_vel
    data["eye_movement_amp_given"] = event_amp_given
    data["eye_movement_duration"] = event_duration
