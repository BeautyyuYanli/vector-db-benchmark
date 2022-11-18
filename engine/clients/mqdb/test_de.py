from typing import List, Tuple

from myscaledb import Client

from engine.clients.mqdb.config import *


def getRe() -> List[Tuple[int, float]]:
    client = Client(url='http://{}:{}/'.format("10.10.1.51", 8123),
                    user="default",
                    password="")
    # result = client.fetch(
    #     "SELECT id, distance('topK=10')(vector, \
    #     [0.47436523,-0.2142334,0.63134766,-0.70410156,0.25732422,0.25097656,-0.17712402,0.046417236,-0.7211914,-0.1517334,0.042938232,0.14990234,-0.3137207,0.84521484,0.7988281,-0.17712402,0.31469727,-0.08734131,-0.38964844,0.17712402,0.4658203,-0.02835083,-0.5888672,-0.22351074,0.20080566,0.04107666,0.049468994,0.10021973,-0.29589844,-0.02885437,-0.019363403,-0.15283203,0.2722168,-0.10076904,0.014671326,0.26098633,0.39697266,-0.0052757263,0.4025879,-0.1340332,0.17272949,0.27441406,0.36767578,-0.12011719,-0.23010254,-0.087768555,-0.25805664,0.1920166,0.6069336,-0.19677734,-0.26220703,-0.7871094,-0.82177734,0.024368286,1.1083984,-0.15942383,-0.5136719,0.8222656,0.015258789,0.34521484,0.111328125,-0.19628906,0.17944336,-0.5395508,0.31640625,0.44262695,0.13537598,-0.46020508,0.14587402,0.17700195,-0.45336914,-0.5600586,-0.75927734,-0.23376465,-1.0039062,-0.56396484,-0.14562988,0.058929443,0.5307617,0.020507812,-0.5957031,0.14221191,-0.13183594,0.90283203,-0.55566406,0.69677734,-0.0037136078,0.10522461,-0.34594727,-0.8203125,-0.38183594,-0.35791016,0.04916382,0.028137207,0.08441162,0.2861328,-0.6074219,-0.43017578,-0.2434082,-0.3774414,-0.31982422,0.18554688,-0.9199219,0.81591797,-0.048614502,-0.6826172,-0.34472656,0.5917969,-0.02255249,-0.25048828,-0.6166992,0.18249512,-0.26391602,-0.32543945,-0.11798096,0.5214844,-0.8251953,-0.5029297,0.3203125,0.10668945,-0.19421387,0.076293945,0.38232422,-0.7553711,-0.0061035156,-0.39990234,0.45654297,0.9711914,-0.67578125,0.085632324,0.24743652,0.88378906,-0.48876953,-0.18725586,-0.04940796,-0.074279785,0.32788086,-0.5126953,0.4921875,0.94140625,-0.024719238,-0.3605957,-0.7050781,-0.50341797,-1.1484375,0.35668945,-0.019882202,-0.7324219,0.57373047,-0.12207031,-0.38500977,-0.38208008,0.40673828,0.49121094,0.5576172,1.3320312,-0.19714355,-0.28173828,-0.12084961,0.04434204,0.5708008,-0.14416504,0.19299316,0.5961914,0.11755371,-0.05328369,0.10461426,0.37939453,-0.23669434,-0.27001953,0.46850586,-0.5498047,-0.17016602,0.64746094,0.05593872,-0.03479004,0.08526611,0.46557617,-0.28051758,-0.011451721,0.68652344,-0.8564453,-0.55859375,0.4404297,0.06744385,-0.83691406,0.82910156,0.74072266,-0.15148926,0.2121582,0.6196289,0.4428711,-0.14208984,0.09454346,0.12683105,0.089538574,-0.42749023,-0.5136719,0.2421875,0.4794922,-0.42773438,-0.13427734,0.18847656,-0.2064209,0.054718018,0.3803711,-0.41015625,-0.04901123,0.5205078,0.103149414,-0.2355957,-0.74121094,0.51904297,0.44067383,-0.023483276,-0.5541992,0.17333984,1.1240234,-0.09692383,-0.33935547,-0.26635742,-0.45385742,-5.203125,-0.96533203,-0.21374512,0.6567383,-0.30981445,-0.2088623,0.4807129,-0.099121094,1.0078125,0.81640625,0.067993164,0.58447266,-0.27612305,0.19641113,-0.44360352,-0.7373047,-0.12158203,-0.03111267,1.3349609,0.09313965,-0.07080078,0.35595703,0.101989746,0.6464844,-0.26367188,0.5366211,-0.96191406,0.5209961,-0.14489746,0.5073242,0.5834961,-0.8173828,-0.21520996,0.23693848,-0.45043945,1.6181641,-0.3190918,-0.5053711,0.55810547,-0.5078125,-0.18444824,0.2998047,0.25268555,-0.5439453,0.9169922,0.2322998,-0.06829834,0.08135986,0.4255371,0.61376953,0.04220581,-0.48217773,-0.15771484,0.45776367,-0.7314453,-0.4765625,0.05429077,-0.2932129,-0.34594727,-0.032043457,-0.47583008,-0.39111328,0.7006836,-0.5644531,0.32470703,-0.7446289,0.17443848,0.45898438,-0.38061523,-0.05053711,-0.06921387,-0.6767578,-0.57910156,0.29174805,-0.6376953,-0.35424805,-0.2421875,-0.49414062,0.27612305,-0.4333496,0.28051758,-0.63427734,0.48486328,-0.0009217262,-0.4177246,0.2746582,0.028900146,-0.31835938,-0.2553711,0.23046875,-0.001660347,0.34545898,0.56396484,0.37426758,-0.12731934,-0.1619873,0.8173828,-0.08496094,0.39501953,0.63720703,-0.86376953,-0.0069999695,-0.41723633,-0.703125,-0.29077148,-0.40234375,-0.66796875,0.40600586,-0.045043945,-0.3083496,-0.02722168,0.048950195,-0.09112549,-0.97998047,0.69921875,0.30078125,0.46606445,0.06555176,0.23608398,0.21582031,0.1517334,0.04171753,0.19299316,0.029006958,-0.016494751,0.40722656,-0.12548828,-0.16882324,0.0791626,-0.36987305,0.72998047,0.15026855,-0.082092285,-0.7636719,-0.84375,0.17529297,0.10681152,0.49902344,-0.011116028,0.69677734,0.47631836,0.13671875,-0.37548828,0.28320312,-0.19250488,0.7861328,0.2512207,-0.54589844,-0.8461914,-0.26464844,0.38720703,-0.56347656,0.3540039,-0.085510254,0.11529541,-0.20800781,0.69433594,0.6225586,0.07904053,0.17419434,0.51416016,-0.7006836,-0.7036133,-0.20776367,0.03466797,-0.039886475,0.45898438,-0.1529541,-0.13427734,-0.6152344,-0.65283203,-0.011398315,-0.15612793,-0.07446289,-0.3095703,-0.47460938,-0.39282227,0.06964111,0.25585938,0.21130371,0.33520508,-0.026565552,-0.15063477,0.13098145,-0.30078125,0.28173828,-0.055389404,0.44506836,-0.12561035,-0.2409668,0.05505371,0.43359375,0.21008301,-0.1661377,-0.23217773,-0.40039062,-0.054351807,0.059020996,0.65966797,-0.21582031,0.14709473,-0.3479004,-0.059051514,0.13317871,-0.37060547,-1.2246094,-0.22241211,-0.14526367,-0.3486328,0.2919922,-1.1337891,0.18591309,-0.04272461,0.95214844,-0.43310547,0.14221191,0.15112305,0.070373535,0.119262695,0.71484375,0.2841797,-0.26635742,-0.56103516,0.45703125,0.8876953,0.20788574,-0.10656738,0.37646484,-0.4543457,-0.65966797,-0.07104492,0.07672119,0.4152832,-0.82373047,-0.095214844,-0.11444092,-0.050598145,-0.22436523,0.9243164,0.18518066,-0.14733887,-0.34521484,-0.35083008,0.34155273,0.12207031,-0.10998535,-0.78808594,-0.06518555,-0.0041885376,-0.10699463,0.25830078,0.9873047,0.061279297,-0.19543457,-0.31933594,0.33764648,0.15405273,-0.84765625,-0.041137695,-0.010681152,-0.24926758,-0.1239624,-0.14196777,-0.24255371,-0.04232788,0.09515381,0.5839844,-0.3251953,-0.002450943,0.050994873,-0.60546875,-0.2142334,-0.5449219,0.07751465,0.57421875,-0.2800293,-0.090026855,-0.10638428,-0.1973877,0.21411133,0.43652344,0.4892578,-0.99121094,1.0244141,-0.22924805,0.35083008,0.31567383,-0.7949219,0.46557617,0.23266602,-0.6323242,0.6796875,0.2019043,-0.43798828,0.54833984,-0.19091797,-0.18933105,-0.26098633,0.20593262,0.085510254,-0.18664551,-0.66503906,0.20495605,-0.118652344,-0.5683594,-0.3215332,-0.48242188,0.18737793,0.12609863,0.12017822,0.62939453,0.28710938,-0.26635742,-0.33447266,-0.07165527,0.17114258,-0.23925781,-0.23132324,-0.37597656,-0.02243042,0.05682373,0.60498047,0.32910156,0.049682617,-0.12109375,0.17553711,-0.33544922,0.022247314,-1.515625,0.018630981,-0.34423828,-0.16479492,-0.16552734,0.21557617,-0.22961426,-0.4716797,-0.045440674,0.6401367,0.021942139,0.34985352,0.6303711,-0.12731934,0.026367188,-0.1665039,-0.054656982,0.5527344,-0.33569336,-0.38061523,0.56347656,-0.057556152,-0.028686523,0.76123047,0.051818848,0.64990234,0.018859863,0.28173828,0.43847656,0.01550293,0.49804688,-0.15979004,-0.33154297,-0.5834961,-0.23950195,-0.80615234,0.4724121,0.41601562,-0.33862305,0.1027832,-0.74658203,0.35009766,0.45263672,-0.79003906,0.1237793,0.1763916,0.0635376,-0.19226074,-0.0009522438,0.42822266,0.69677734,0.16723633,0.29907227,0.11273193,0.39892578,0.07922363,0.11456299,1.0810547,0.08325195,0.20837402,0.33911133,0.05407715,0.8676758,0.05593872,-0.07977295,-0.25854492,-0.14245605,-0.07635498,-0.20654297,-0.0052490234,0.26220703,-0.6274414,0.9033203,-0.19592285,-0.40576172,0.74902344,-0.34692383,0.38623047,0.31958008,0.2644043,0.05697632,-0.39770508,-0.13012695,-0.05834961,-0.76953125,-0.2890625,0.3166504,0.22888184,0.08270264,-0.33544922,0.42114258,0.17932129,0.3864746,0.0904541,0.41625977,-0.04916382,0.19250488,0.2939453,-0.2211914,0.5317383,-0.5239258,-0.045043945,0.015464783,-0.3696289,0.08001709,-0.3486328,-0.35083008,-1.1015625,-0.2064209,0.3696289,-0.30810547,-0.39013672,0.59277344,-0.2932129,0.6928711,-0.13708496,-0.12658691,-0.1706543,0.4206543,0.003698349,-0.2775879,0.56103516,0.39990234,-0.086242676,0.15905762,-0.94873047,0.68847656,-0.375,0.43041992,-0.0036239624,-0.03012085,0.2932129,-0.6015625,0.021133423,-0.045776367,0.44360352,-0.22338867,-0.83203125,-1.0058594,-0.49609375,-0.19934082,-0.125,-0.17712402,0.124694824,-1.0019531,0.44995117,-0.024215698,0.26391602,0.7763672,0.57714844,-0.014884949,0.33764648,-0.15270996,0.033447266,-0.075683594,0.07525635,0.4260254,-0.20739746,-0.45263672,-0.101989746,-0.08026123,0.7753906,-0.6381836,-0.41259766,-0.26416016,-0.13464355,-0.45581055,-0.65722656,-0.21899414,0.13342285,0.99365234,-0.19140625,0.44262695,0.42407227,1.2685547,0.07550049,0.33544922,-0.63916016,0.3527832,-0.33935547,0.09124756,0.41479492,0.18127441,-0.27954102,0.47045898,0.5126953,-0.55029297,0.13354492,0.09289551,-0.67626953,-0.078430176,0.39404297,-0.15576172,0.025482178,-0.30737305,0.35253906,-0.07891846,-0.15222168,-0.5292969,-0.32983398,-0.07019043,0.59033203,-0.13354492,0.13269043,0.13537598,-0.52978516,-0.070373535,-0.047943115,-0.2734375,-0.7558594,0.016525269,0.22875977,-0.3815918,0.43066406,-0.34472656,-0.27929688,-0.5083008,-0.12646484]) as dis FROM testdata_sq_16_256_rc1"
    # )

    # result = client.fetch(
    #     query="SELECT id, distance('topK=10')(vector, [0.47436523,-0.2142334,0.63134766,-0.70410156,0.25732422,0.25097656,-0.17712402,0.046417236,-0.7211914,-0.1517334,0.042938232,0.14990234,-0.3137207,0.84521484,0.7988281,-0.17712402,0.31469727,-0.08734131,-0.38964844,0.17712402,0.4658203,-0.02835083,-0.5888672,-0.22351074,0.20080566,0.04107666,0.049468994,0.10021973,-0.29589844,-0.02885437,-0.019363403,-0.15283203,0.2722168,-0.10076904,0.014671326,0.26098633,0.39697266,-0.0052757263,0.4025879,-0.1340332,0.17272949,0.27441406,0.36767578,-0.12011719,-0.23010254,-0.087768555,-0.25805664,0.1920166,0.6069336,-0.19677734,-0.26220703,-0.7871094,-0.82177734,0.024368286,1.1083984,-0.15942383,-0.5136719,0.8222656,0.015258789,0.34521484,0.111328125,-0.19628906,0.17944336,-0.5395508,0.31640625,0.44262695,0.13537598,-0.46020508,0.14587402,0.17700195,-0.45336914,-0.5600586,-0.75927734,-0.23376465,-1.0039062,-0.56396484,-0.14562988,0.058929443,0.5307617,0.020507812,-0.5957031,0.14221191,-0.13183594,0.90283203,-0.55566406,0.69677734,-0.0037136078,0.10522461,-0.34594727,-0.8203125,-0.38183594,-0.35791016,0.04916382,0.028137207,0.08441162,0.2861328,-0.6074219,-0.43017578,-0.2434082,-0.3774414,-0.31982422,0.18554688,-0.9199219,0.81591797,-0.048614502,-0.6826172,-0.34472656,0.5917969,-0.02255249,-0.25048828,-0.6166992,0.18249512,-0.26391602,-0.32543945,-0.11798096,0.5214844,-0.8251953,-0.5029297,0.3203125,0.10668945,-0.19421387,0.076293945,0.38232422,-0.7553711,-0.0061035156,-0.39990234,0.45654297,0.9711914,-0.67578125,0.085632324,0.24743652,0.88378906,-0.48876953,-0.18725586,-0.04940796,-0.074279785,0.32788086,-0.5126953,0.4921875,0.94140625,-0.024719238,-0.3605957,-0.7050781,-0.50341797,-1.1484375,0.35668945,-0.019882202,-0.7324219,0.57373047,-0.12207031,-0.38500977,-0.38208008,0.40673828,0.49121094,0.5576172,1.3320312,-0.19714355,-0.28173828,-0.12084961,0.04434204,0.5708008,-0.14416504,0.19299316,0.5961914,0.11755371,-0.05328369,0.10461426,0.37939453,-0.23669434,-0.27001953,0.46850586,-0.5498047,-0.17016602,0.64746094,0.05593872,-0.03479004,0.08526611,0.46557617,-0.28051758,-0.011451721,0.68652344,-0.8564453,-0.55859375,0.4404297,0.06744385,-0.83691406,0.82910156,0.74072266,-0.15148926,0.2121582,0.6196289,0.4428711,-0.14208984,0.09454346,0.12683105,0.089538574,-0.42749023,-0.5136719,0.2421875,0.4794922,-0.42773438,-0.13427734,0.18847656,-0.2064209,0.054718018,0.3803711,-0.41015625,-0.04901123,0.5205078,0.103149414,-0.2355957,-0.74121094,0.51904297,0.44067383,-0.023483276,-0.5541992,0.17333984,1.1240234,-0.09692383,-0.33935547,-0.26635742,-0.45385742,-5.203125,-0.96533203,-0.21374512,0.6567383,-0.30981445,-0.2088623,0.4807129,-0.099121094,1.0078125,0.81640625,0.067993164,0.58447266,-0.27612305,0.19641113,-0.44360352,-0.7373047,-0.12158203,-0.03111267,1.3349609,0.09313965,-0.07080078,0.35595703,0.101989746,0.6464844,-0.26367188,0.5366211,-0.96191406,0.5209961,-0.14489746,0.5073242,0.5834961,-0.8173828,-0.21520996,0.23693848,-0.45043945,1.6181641,-0.3190918,-0.5053711,0.55810547,-0.5078125,-0.18444824,0.2998047,0.25268555,-0.5439453,0.9169922,0.2322998,-0.06829834,0.08135986,0.4255371,0.61376953,0.04220581,-0.48217773,-0.15771484,0.45776367,-0.7314453,-0.4765625,0.05429077,-0.2932129,-0.34594727,-0.032043457,-0.47583008,-0.39111328,0.7006836,-0.5644531,0.32470703,-0.7446289,0.17443848,0.45898438,-0.38061523,-0.05053711,-0.06921387,-0.6767578,-0.57910156,0.29174805,-0.6376953,-0.35424805,-0.2421875,-0.49414062,0.27612305,-0.4333496,0.28051758,-0.63427734,0.48486328,-0.0009217262,-0.4177246,0.2746582,0.028900146,-0.31835938,-0.2553711,0.23046875,-0.001660347,0.34545898,0.56396484,0.37426758,-0.12731934,-0.1619873,0.8173828,-0.08496094,0.39501953,0.63720703,-0.86376953,-0.0069999695,-0.41723633,-0.703125,-0.29077148,-0.40234375,-0.66796875,0.40600586,-0.045043945,-0.3083496,-0.02722168,0.048950195,-0.09112549,-0.97998047,0.69921875,0.30078125,0.46606445,0.06555176,0.23608398,0.21582031,0.1517334,0.04171753,0.19299316,0.029006958,-0.016494751,0.40722656,-0.12548828,-0.16882324,0.0791626,-0.36987305,0.72998047,0.15026855,-0.082092285,-0.7636719,-0.84375,0.17529297,0.10681152,0.49902344,-0.011116028,0.69677734,0.47631836,0.13671875,-0.37548828,0.28320312,-0.19250488,0.7861328,0.2512207,-0.54589844,-0.8461914,-0.26464844,0.38720703,-0.56347656,0.3540039,-0.085510254,0.11529541,-0.20800781,0.69433594,0.6225586,0.07904053,0.17419434,0.51416016,-0.7006836,-0.7036133,-0.20776367,0.03466797,-0.039886475,0.45898438,-0.1529541,-0.13427734,-0.6152344,-0.65283203,-0.011398315,-0.15612793,-0.07446289,-0.3095703,-0.47460938,-0.39282227,0.06964111,0.25585938,0.21130371,0.33520508,-0.026565552,-0.15063477,0.13098145,-0.30078125,0.28173828,-0.055389404,0.44506836,-0.12561035,-0.2409668,0.05505371,0.43359375,0.21008301,-0.1661377,-0.23217773,-0.40039062,-0.054351807,0.059020996,0.65966797,-0.21582031,0.14709473,-0.3479004,-0.059051514,0.13317871,-0.37060547,-1.2246094,-0.22241211,-0.14526367,-0.3486328,0.2919922,-1.1337891,0.18591309,-0.04272461,0.95214844,-0.43310547,0.14221191,0.15112305,0.070373535,0.119262695,0.71484375,0.2841797,-0.26635742,-0.56103516,0.45703125,0.8876953,0.20788574,-0.10656738,0.37646484,-0.4543457,-0.65966797,-0.07104492,0.07672119,0.4152832,-0.82373047,-0.095214844,-0.11444092,-0.050598145,-0.22436523,0.9243164,0.18518066,-0.14733887,-0.34521484,-0.35083008,0.34155273,0.12207031,-0.10998535,-0.78808594,-0.06518555,-0.0041885376,-0.10699463,0.25830078,0.9873047,0.061279297,-0.19543457,-0.31933594,0.33764648,0.15405273,-0.84765625,-0.041137695,-0.010681152,-0.24926758,-0.1239624,-0.14196777,-0.24255371,-0.04232788,0.09515381,0.5839844,-0.3251953,-0.002450943,0.050994873,-0.60546875,-0.2142334,-0.5449219,0.07751465,0.57421875,-0.2800293,-0.090026855,-0.10638428,-0.1973877,0.21411133,0.43652344,0.4892578,-0.99121094,1.0244141,-0.22924805,0.35083008,0.31567383,-0.7949219,0.46557617,0.23266602,-0.6323242,0.6796875,0.2019043,-0.43798828,0.54833984,-0.19091797,-0.18933105,-0.26098633,0.20593262,0.085510254,-0.18664551,-0.66503906,0.20495605,-0.118652344,-0.5683594,-0.3215332,-0.48242188,0.18737793,0.12609863,0.12017822,0.62939453,0.28710938,-0.26635742,-0.33447266,-0.07165527,0.17114258,-0.23925781,-0.23132324,-0.37597656,-0.02243042,0.05682373,0.60498047,0.32910156,0.049682617,-0.12109375,0.17553711,-0.33544922,0.022247314,-1.515625,0.018630981,-0.34423828,-0.16479492,-0.16552734,0.21557617,-0.22961426,-0.4716797,-0.045440674,0.6401367,0.021942139,0.34985352,0.6303711,-0.12731934,0.026367188,-0.1665039,-0.054656982,0.5527344,-0.33569336,-0.38061523,0.56347656,-0.057556152,-0.028686523,0.76123047,0.051818848,0.64990234,0.018859863,0.28173828,0.43847656,0.01550293,0.49804688,-0.15979004,-0.33154297,-0.5834961,-0.23950195,-0.80615234,0.4724121,0.41601562,-0.33862305,0.1027832,-0.74658203,0.35009766,0.45263672,-0.79003906,0.1237793,0.1763916,0.0635376,-0.19226074,-0.0009522438,0.42822266,0.69677734,0.16723633,0.29907227,0.11273193,0.39892578,0.07922363,0.11456299,1.0810547,0.08325195,0.20837402,0.33911133,0.05407715,0.8676758,0.05593872,-0.07977295,-0.25854492,-0.14245605,-0.07635498,-0.20654297,-0.0052490234,0.26220703,-0.6274414,0.9033203,-0.19592285,-0.40576172,0.74902344,-0.34692383,0.38623047,0.31958008,0.2644043,0.05697632,-0.39770508,-0.13012695,-0.05834961,-0.76953125,-0.2890625,0.3166504,0.22888184,0.08270264,-0.33544922,0.42114258,0.17932129,0.3864746,0.0904541,0.41625977,-0.04916382,0.19250488,0.2939453,-0.2211914,0.5317383,-0.5239258,-0.045043945,0.015464783,-0.3696289,0.08001709,-0.3486328,-0.35083008,-1.1015625,-0.2064209,0.3696289,-0.30810547,-0.39013672,0.59277344,-0.2932129,0.6928711,-0.13708496,-0.12658691,-0.1706543,0.4206543,0.003698349,-0.2775879,0.56103516,0.39990234,-0.086242676,0.15905762,-0.94873047,0.68847656,-0.375,0.43041992,-0.0036239624,-0.03012085,0.2932129,-0.6015625,0.021133423,-0.045776367,0.44360352,-0.22338867,-0.83203125,-1.0058594,-0.49609375,-0.19934082,-0.125,-0.17712402,0.124694824,-1.0019531,0.44995117,-0.024215698,0.26391602,0.7763672,0.57714844,-0.014884949,0.33764648,-0.15270996,0.033447266,-0.075683594,0.07525635,0.4260254,-0.20739746,-0.45263672,-0.101989746,-0.08026123,0.7753906,-0.6381836,-0.41259766,-0.26416016,-0.13464355,-0.45581055,-0.65722656,-0.21899414,0.13342285,0.99365234,-0.19140625,0.44262695,0.42407227,1.2685547,0.07550049,0.33544922,-0.63916016,0.3527832,-0.33935547,0.09124756,0.41479492,0.18127441,-0.27954102,0.47045898,0.5126953,-0.55029297,0.13354492,0.09289551,-0.67626953,-0.078430176,0.39404297,-0.15576172,0.025482178,-0.30737305,0.35253906,-0.07891846,-0.15222168,-0.5292969,-0.32983398,-0.07019043,0.59033203,-0.13354492,0.13269043,0.13537598,-0.52978516,-0.070373535,-0.047943115,-0.2734375,-0.7558594,0.016525269,0.22875977,-0.3815918,0.43066406,-0.34472656,-0.27929688,-0.5083008,-0.12646484]) as dis FROM testdata_sq_16_256_rc1"
    # )

    result = client.fetch(
        query="SELECT id, distance('topK=10')(vector,[-0.17031723260879517, -0.0901658907532692, 0.1413794457912445, 0.02499842643737793, -0.2620302438735962, -0.3631281554698944, -0.5163598656654358, -0.2071089744567871, 0.09339465200901031, -0.296292781829834, -0.08437563478946686, 0.17819271981716156, 0.029648112133145332, -0.1892404705286026, 0.27334168553352356, -0.034655388444662094, 0.10154996812343597, 0.09607183188199997, -0.03102302737534046, 0.052542731165885925, 0.09711042046546936, 0.24851247668266296, -0.24839408695697784, 0.11325962096452713, 0.12341945618391037]) as dis FROM Benchmark"
    )
    result_list = []
    for i in result:
        print(dict(i))
        # print(list(zip(dict(i).keys(),dict(i).values())))
        print(tuple(dict(i).values()))
        result_list.append((int(dict(i).get('id')), float(dict(i).get('dis'))))
    return result_list
    # return list(zip(result.))


print(getRe())

index_parameter_str = "'metric_type={}'".format("IP")
print(index_parameter_str)
