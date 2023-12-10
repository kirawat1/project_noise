import argparse

parser = argparse.ArgumentParser(description='Speech enhancement,data creation, training and prediction')

#mode to run the program (options: data creation, training or prediction)
parser.add_argument('--mode',default='prediction', type=str, choices=['data_creation', 'training', 'prediction'])
# 
parser.add_argument('--noise_dir', default='D:\\CS\\Project_\\Train\\noise', type=str)
#
parser.add_argument('--voice_dir', default='D:\\CS\\Project_\\Train\\clean_voice', type=str)
# 
parser.add_argument('--path_save_spectrogram', default='D:\\CS\\Project_\\Train\\spectrogram', type=str)
# 
parser.add_argument('--path_save_time_serie', default='D:\\CS\\Project_\\Train\\time_serie', type=str)
#
parser.add_argument('--path_save_sound', default='D:\\CS\\Project_\\Train\\sound', type=str)

parser.add_argument('--sample_rate', default=8000, type=int)
# Minimum duration of audio files to consider
parser.add_argument('--min_duration', default=1.0, type=float)
# Training data will be frame of slightly above 1 second
parser.add_argument('--frame_length', default=8064, type=int)
# hop length for clean voice files separation (no overlap)
parser.add_argument('--hop_length_frame', default=8064, type=int)
# hop length for noise files to blend (noise is splitted into several windows)
parser.add_argument('--hop_length_frame_noise', default=5000, type=int)
#How much frame to create in data_creation mode (0.50 sec)
parser.add_argument('--nb_samples', default=50, type=int)
# Choosing n_fft and hop_length_fft to have squared spectrograms
parser.add_argument('--n_fft', default=255, type=int)
parser.add_argument('--hop_length_fft', default=63, type=int)
#Noisy sound file to denoise (prediction mode)
parser.add_argument('--audio_input_prediction', default=['noisy_voice_long_t2.wav'], type=list)