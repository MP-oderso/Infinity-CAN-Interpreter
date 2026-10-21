#mit KI-unterstützung aus rohdaten extrahiert 
#fehlen einer weiteren dimension um zeitlichen verlauf der messungen darzustellen, daher nur einzelne messungen in einer liste
Messungen = [
    {"CAN_Message":"steering_travel"    ,"unit":"mm"    ,"value":23.69  ,"timestamp":"2026-09-27T15:33:56Z" ,"signal":"SMU_STR_travel"      ,"message":"SMU_STR_data_1" ,"can_id":"0x31E"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
    {"CAN_Message":"vehicle_speed"      ,"unit":"km/h"  ,"value":38.5   ,"timestamp":"2026-09-27T15:33:56Z" ,"signal":"VCU_speed"           ,"message":"VCU_speed"      ,"can_id":"0x700"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
    {"CAN_Message":"wheel_rpm_fr"       ,"unit":"rpm"   ,"value":534.5  ,"timestamp":"2026-09-27T15:33:56Z" ,"signal":"SMU_FR_wheelspeed"   ,"message":"SMU_FR_data_3"  ,"can_id":"0x317"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
    {"CAN_Message":"wheel_rpm_fl"       ,"unit":"rpm"   ,"value":505.4  ,"timestamp":"2026-09-27T15:33:56Z" ,"signal":"SMU_FL_wheelspeed"   ,"message":"SMU_FL_data_3"  ,"can_id":"0x315"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
    {"CAN_Message":"accumulator_SOC"    ,"unit":"%"     ,"value":44.0   ,"timestamp":"2026-09-27T15:34:36Z" ,"signal":"AMS_soc"             ,"message":"AMS_state"      ,"can_id":"0x200"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
    {"CAN_Message":"steering_travel"    ,"unit":"mm"    ,"value":30.82  ,"timestamp":"2026-09-27T15:35:56Z" ,"signal":"SMU_STR_travel"      ,"message":"SMU_STR_data_1" ,"can_id":"0x31E"   ,"bus":1    ,"source_file":"Measurement_25.mat"},
   ]

if __name__ == "__main__":
    for messung in Messungen:
        print(f"Messung: {messung['CAN_Message']}, Wert: {messung['value']} {messung['unit']}, Zeitstempel: {messung['timestamp']}")