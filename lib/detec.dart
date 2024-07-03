import 'dart:convert';
import 'dart:io';

import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Voice Recorder & Audio Upload',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const AudioDetectionScreen(),
    );
  }
}

class AudioDetectionScreen extends StatefulWidget {
  const AudioDetectionScreen({super.key});

  @override
  AudioDetectionScreenState createState() => AudioDetectionScreenState();
}

class AudioDetectionScreenState extends State<AudioDetectionScreen> {
  File? selectedFile;
  String? detectionResult;
  bool isLoading = false;

  final Map<String, String> emotionImages = {
    // 'neutral': 'assets/images/neutral.png',
    // 'calm': 'assets/images/calm.png',
    // 'happy': 'assets/images/happy.png',
    // 'sad': 'assets/images/sad.png',
    'angry': 'assets/images/angry.jpg',
    // 'fearful': 'assets/images/fearful.png',
    // 'disgust': 'assets/images/disgust.png',
    // 'surprised': 'assets/images/surprised.png',
    // 'Detection error': 'assets/images/error.png',
  };

  final Map<String, String> emotionQuotes = {
    'neutral': 'Stay calm and carry on.',
    'calm': 'Peace comes from within.',
    'happy': 'Happiness is the key to success.',
    'sad': 'Tears are words the heart can’t express.',
    'angry': 'Anger is one letter short of danger.',
    'fearful': 'Do not let your fears choose your destiny.',
    'disgust': 'Disgust is a moral emotion.',
    'surprised': 'Surprises are the joy of life.',
    'Detection error': 'Detection error occurred. Please try again.',
  };

  Future<void> pickAudioFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['mp3', 'wav', 'aac'],
    );

    if (result != null) {
      setState(() {
        selectedFile = File(result.files.single.path!);
        detectionResult = null; // Reset detection result on new file selection
      });
    }
  }

  Future<void> sendForDetection() async {
    if (selectedFile == null) return;

    setState(() {
      isLoading = true;
    });

    var request = http.MultipartRequest('POST', Uri.parse('http://192.168.4.105:8080/analyse_audio'));
    request.files.add(await http.MultipartFile.fromPath(
      'audio',
      selectedFile!.path,
    ));

    var response = await request.send();
    if (response.statusCode == 200) {
      var responseData = await response.stream.bytesToString();
      var jsonResponse = json.decode(responseData);
      String prediction = jsonResponse['prediction'];

      setState(() {
        detectionResult = prediction;
        isLoading = false;
      });
    } else {
      setState(() {
        detectionResult = 'Detection error';
        isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Emotion Detection'),
        backgroundColor: Colors.blueAccent,
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Image.asset(
                'assets/images/here.png', // Add your image asset here
                height: 150,
              ),
              const SizedBox(height: 10),
              ElevatedButton.icon(
                onPressed: pickAudioFile,
                icon: const Icon(Icons.audiotrack),
                label: const Text('Select an audio recording'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.blueAccent,
                  padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
                  textStyle: const TextStyle(fontSize: 11),
                ),
              ),
              const SizedBox(height: 20),
              if (selectedFile != null)
                Text(
                  'Selected file: ${selectedFile!.path.split('/').last}',
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.w500),
                ),
              const SizedBox(height: 20),
              ElevatedButton.icon(
                onPressed: isLoading ? null : sendForDetection,
                icon: const Icon(Icons.send),
                label: const Text('Start detection'),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green,
                  padding: const EdgeInsets.symmetric(horizontal: 30, vertical: 15),
                  textStyle: const TextStyle(fontSize: 16),
                ),
              ),
              const SizedBox(height: 20),
              if (isLoading)
                const CircularProgressIndicator(),
              if (detectionResult != null)
                Column(
                  children: [
                    Image.asset(
                      emotionImages[detectionResult]!,
                      height: 100,
                      width: 100,
                    ),
                    const SizedBox(height: 10),
                    Text(
                      'Result: $detectionResult',
                      style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.black87),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 10),
                    Text(
                      emotionQuotes[detectionResult]!,
                      style: const TextStyle(fontSize: 16, fontStyle: FontStyle.italic, color: Colors.grey),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
            ],
          ),
        ),
      ),
    );
  }
}
