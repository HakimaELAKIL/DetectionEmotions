// import 'package:audioplayers/audioplayers.dart';
// import 'package:file_picker/file_picker.dart';
// import 'package:flutter/material.dart';
// import 'package:path_provider/path_provider.dart';
// import 'package:record/record.dart';

// import 'detec.dart';
// void main() {
//   runApp(const MyApp());
// }


// class MyApp extends StatelessWidget {
//   const MyApp({super.key}); // Constructor

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: 'Voice Recorder & Audio Upload', // Title of the app
//       theme: ThemeData(
//         primarySwatch: Colors.blue, // Theme color
//       ),
//       home: const MyHomePage(), // Default route, mapped to MyHomePage
//       initialRoute: '/', // Initial route to load when the app starts
//       routes: {
//         '/detec': (context) => const AudioDetectionScreen(), // Named route for AudioDetectionScreen
//       },
//     );
//   }
// }




// class MyHomePage extends StatefulWidget {
//   const MyHomePage({super.key});

//   @override
//   // ignore: library_private_types_in_public_api
//   _MyHomePageState createState() => _MyHomePageState();

// }

// class _MyHomePageState extends State<MyHomePage> {
//   final AudioPlayer audioPlayer = AudioPlayer();
//   final Record recorder = Record();
//   bool isRecording = false;
//   String? filePath;
//   // final Record _recorder = Record();
//   // bool _isRecording = false;
//   // String? _filePath;
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text('Voice Recorder & Audio Upload'),
//       ),
//       body: Column(
//         mainAxisAlignment: MainAxisAlignment.center,
//         children: <Widget>[
//           if (isRecording)
//             const Icon(Icons.fiber_manual_record, color: Colors.red, size: 30), // Icône de signalisation d'enregistrement
//           Expanded(
//             child: Center(
//               child: Row(
//                 mainAxisAlignment: MainAxisAlignment.center,
//                 children: <Widget>[
//                   //   ElevatedButton.icon(
//                   //   onPressed: () {
//                   //     if (isRecording) {
//                   //       stopRecording();
//                   //     } else {
//                   //       startRecording();
//                   //     }
//                   //   },
//                   //   icon: Icon(
//                   //     isRecording ? Icons.stop : Icons.mic,
//                   //     color: Colors.white,
//                   //   ),
//                   //   label: Text(
//                   //     isRecording ? 'A' : 'C',
//                   //     style: const TextStyle(color: Colors.white),
//                   //   ),
//                   //   style: ElevatedButton.styleFrom(
//                   //     backgroundColor: isRecording ? Colors.red : Colors.blue,
//                   //   ),
//                   // ),
//                   // Bouton personnalisé pour l'enregistrement
//                   ElevatedButton.icon(
//                     onPressed: () {
//                       if (isRecording) {
//                         stopRecording();
//                       } else {
//                         startRecording();
//                       }
//                     },
//                     icon: Icon(
//                       isRecording ? Icons.stop : Icons.mic,
//                       color: Colors.white,
//                     ),
//                     label: Text(
//                       isRecording ? 'Arrêter' : 'Commencer',
//                       style: const TextStyle(color: Color.fromRGBO(255, 255, 255, 1)),
//                     ),
//                     style: ElevatedButton.styleFrom(
//                       backgroundColor: isRecording ? Colors.red : Colors.blue,
//                     ),
//                   ),
                  
//                   const SizedBox(width: 8), // Espacement entre les boutons
//                   // Bouton personnalisé pour télécharger l'audio
//                   ElevatedButton.icon(
//                     onPressed: uploadAudio,
//                     icon: const Icon(
//                       Icons.upload_file,
//                       color: Colors.white,
//                     ),
//                     label: const Text(
//                       'Télécharger l\'Audio',
//                       style: TextStyle(color: Colors.white),
//                     ),
//                     style: ElevatedButton.styleFrom(
//                       backgroundColor: Colors.green,
//                     ),
//                   ),
//                 ],
//               ),
//             ),
//           ),
//           const SizedBox(height: 5), // Espacement entre les lignes
//           // Bouton personnalisé pour la navigation
//           ElevatedButton(
//             onPressed: () {
//               Navigator.pushNamed(context, '/detec');
//             },
//             child: const Text('Aller à l\'écran de détection audio'),
//           ),
//         ],
//       ),
//     );
//   }

// // Future<void> _start() async {
// //     try {
// //       if (await _recorder.hasPermission()) {
// //         final directory = await getApplicationDocumentsDirectory();
// //         _filePath = '${directory.path}/enregistrement.wav';

// //         await _recorder.start(path: _filePath);
// //         bool isRecording = await _recorder.isRecording();
// //         setState(() {
// //           _isRecording = isRecording;
// //         });
// //       }
// //     } catch (e) {
// //       print(e);
// //     }
// //   }

//   // Future<void> _stop() async {
//   //   await _recorder.stop();
//   //   setState(() {
//   //     _isRecording = false;
//   //   });
//   // }

//   Future<void> startRecording() async {
//     final directory = await getApplicationDocumentsDirectory();
//     filePath = '${directory.path}/flutter_sound.wav';

//     await recorder.start(path: filePath);
//     setState(() {
//       isRecording = true;
//     });
//   }

//   Future<void> stopRecording() async {
//     await recorder.stop();
//     setState(() {
//       isRecording = false;
//     });
//   }

//   Future<void> uploadAudio() async {
//     FilePickerResult? result = await FilePicker.platform.pickFiles();

//     if (result != null) {
//       // Utilisez le fichier sélectionné pour le téléchargement
//       // Exemple : Upload to Firebase Storage
//     } else {
//       // L'utilisateur a annulé la sélection de fichier
//     }
//   }
// }
import 'package:flutter/material.dart';

import 'detec.dart'; // Import the screen for audio detection

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Emotion Detection', // App title
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const EmotionDetectionHomePage(), // Home page for emotion detection
      initialRoute: '/', // Initial route
      routes: {
        '/detec': (context) => const AudioDetectionScreen(), // Route for audio detection screen
      },
    );
  }
}

class EmotionDetectionHomePage extends StatelessWidget {
  const EmotionDetectionHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: <Widget>[
            Image.asset(
              'assets/images/wings.jpg', // Replace with your app logo path
              width: 32,
              height: 32,
            ),
            const SizedBox(width: 10),
            const Text('wings'), // App name
          ],
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Image.asset(
              'assets/images/image.png', // Replace with your image path
              width: 250,
              height: 200,
              fit: BoxFit.cover,
            ),
            const SizedBox(height: 20),
            const Text(
              '"Your emotions are the slaves to your thoughts, and you are the slave to your emotions."',
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 16,
                fontStyle: FontStyle.italic,
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/detec');
              },
              child: const Text('Start Emotion Detection'), // Button to navigate to /detec
            ),
            // Add more widgets related to emotion detection as needed
          ],
        ),
      ),
    );
  }
}
