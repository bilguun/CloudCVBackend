{
    'target_defaults': {
        'default_configuration': 'Release',
    },

    'targets': [
        {
            'target_name': "cloudcv",

            'sources': [ 
                "main.cpp", 
                
                "src/node/node_helpers.hpp", 
                "src/node/node_helpers.cpp",

                "src/modules/node/Marshal.cpp", 
                "src/modules/node/Marshal.hpp",                 

                "src/modules/common/Numeric.cpp", 
                "src/modules/common/Numeric.hpp",                 

                "src/modules/common/Color.hpp", 
                "src/modules/common/Serialization.hpp", 
                "src/modules/common/ScopedTimer.hpp", 

                "src/modules/common/ImageUtils.hpp", 
                "src/modules/common/ImageUtils.cpp", 

                "src/modules/analyze/analyze.cpp", 
                "src/modules/analyze/analyze.hpp", 
                "src/modules/analyze/binding.hpp", 
                "src/modules/analyze/binding.cpp", 
                "src/modules/analyze/dominantColors.hpp", 
                "src/modules/analyze/dominantColors.cpp", 

                "src/modules/faceRec/faceRec.cpp", 
                "src/modules/faceRec/faceRec.hpp", 
                "src/modules/faceRec/faceRecBinding.hpp", 
                "src/modules/faceRec/faceRecBinding.cpp", 

                "src/modules/buildInformation/buildInformation.cpp", 
                "src/modules/buildInformation/buildInformation.hpp", 

                "src/modules/markerDetection/CameraCalibration.cpp",
                "src/modules/markerDetection/CameraCalibration.hpp",
                "src/modules/markerDetection/GeometryTypes.cpp",
                "src/modules/markerDetection/GeometryTypes.hpp",
                "src/modules/markerDetection/Marker.cpp",
                "src/modules/markerDetection/Marker.hpp",
                "src/modules/markerDetection/MarkerDetector.cpp",
                "src/modules/markerDetection/MarkerDetector.hpp",
                "src/modules/markerDetection/TinyLA.cpp",
                "src/modules/markerDetection/TinyLA.hpp",
                "src/modules/markerDetection/MarkerDetectionBinding.cpp",
                "src/modules/markerDetection/MarkerDetectionBinding.hpp",
            ],

            'include_dirs': [
              'src/',
            ],

            'conditions': [
            
                ['OS=="win"', {

                    'configurations': {

                        'Debug': {
                            'defines': [ 'DEBUG', '_DEBUG' ],
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': 2, # static debug
                                },
                            },
                        },

                        'Release': {
                            'defines': [ 'NDEBUG' ],
                            'msvs_settings': {
                                'VCCLCompilerTool': {
                                    'RuntimeLibrary': 2, # static release
                                },
                            },
                        }
                    },

                    'defines': [
                        'TARGET_PLATFORM_WINDOWS',
                    ],

                    'include_dirs': [
                        '$(OPENCV_ROOT)/include'
                    ],

                    'libraries': [
                        "$(OPENCV_ROOT)/lib/opencv_calib3d246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_contrib246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_core246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_features2d246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_flann246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_highgui246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_imgproc246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_legacy246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_ml246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_nonfree246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_objdetect246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_photo246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_stitching246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_superres246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_ts246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_video246.lib",
                        "$(OPENCV_ROOT)/lib/opencv_videostab246.lib",
                        "$(OPENCV_ROOT)/share/OpenCV/3rdparty/lib/libjpeg.lib",
                        "$(OPENCV_ROOT)/share/OpenCV/3rdparty/lib/libpng.lib",
                        "$(OPENCV_ROOT)/share/OpenCV/3rdparty/lib/zlib.lib"
                    ]
                }],

                ['OS=="mac"', {
                
                    'defines': [
                        'TARGET_PLATFORM_MAC',
                    ],

                    'include_dirs': [
                        '/home/bibby/CloudCV/opencv-build/include'
                    ],
                    
                    'libraries': [
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_contrib.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_stitching.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_nonfree.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_ts.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_videostab.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_gpu.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_legacy.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_ml.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_objdetect.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_calib3d.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_photo.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_video.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_features2d.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_highgui.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibtiff.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibpng.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibjpeg.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_flann.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_imgproc.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_core.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/libzlib.a"
                    ],

                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'OTHER_CFLAGS': [ '-g', '-mmacosx-version-min=10.7', '-std=c++11', '-stdlib=libc++', '-O3', '-D__STDC_CONSTANT_MACROS', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE', '-Wall' ],
                        'OTHER_CPLUSPLUSFLAGS': [ '-g', '-mmacosx-version-min=10.7', '-std=c++11', '-stdlib=libc++', '-O3', '-D__STDC_CONSTANT_MACROS', '-D_FILE_OFFSET_BITS=64', '-D_LARGEFILE_SOURCE', '-Wall' ]
                    }
                }],

                
                ['OS=="linux"', {
                
                    'defines': [
                        'TARGET_PLATFORM_LINUX',
                    ],

                    'include_dirs': [
                        '/home/bibby/CloudCV/opencv-build/include'
                    ],
                    
                    'libraries': [
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_contrib.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_stitching.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_nonfree.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_ts.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_videostab.a",
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_gpu.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_legacy.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_ml.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_objdetect.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_calib3d.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_photo.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_video.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_features2d.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_highgui.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibtiff.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibpng.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/liblibjpeg.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_flann.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_imgproc.a", 
                        "/home/bibby/CloudCV/opencv-build/lib/libopencv_core.a", 
                        "/home/bibby/CloudCV/opencv-build/share/OpenCV/3rdparty/lib/libzlib.a"
                    ]
                }]       
            ]
        }
    ]
}
