// const getlocation = () => {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition((position)=> {
//             let lat = position.coords.latitude;
//             let long = position.coords.longitude;
//             console.log("positioon", position)
//         });
//     }
// }

// const getlocation = () => {
//     if (navigator.geolocation) {
//       navigator.permissions.query({ name: 'geolocation' })
//         .then((permissionStatus) => {
//           if (permissionStatus.state === 'granted') {
//             // Permission already granted, proceed with getting location
//             navigator.geolocation.getCurrentPosition(
//               (position) => {
//                 const lat = position.coords.latitude;
//                 const lng = position.coords.longitude;
//                 console.log('Latitude:', lat);
//                 console.log('Longitude:', lng);
//               },
//               (error) => {
//                 console.error('Error occurred while getting location:', error);
//               }
//             );
//           } else if (permissionStatus.state === 'prompt') {
//             // Permission not granted yet, show the prompt
//             permissionStatus.onchange = () => {
//               if (permissionStatus.state === 'granted') {
//                 // Permission granted, proceed with getting location
//                 navigator.geolocation.getCurrentPosition(
//                   (position) => {
//                     const lat = position.coords.latitude;
//                     const lng = position.coords.longitude;
//                     console.log('Latitude:', lat);
//                     console.log('Longitude:', lng);
//                   },
//                   (error) => {
//                     console.error('Error occurred while getting location:', error);
//                   }
//                 );
//               } else {
//                 // Permission denied
//                 console.warn('Location permission denied');
//               }
//             };
//             window.alert('Allow localhost to access your location.');
//           } else {
//             // Permission denied
//             console.warn('Location permission denied');
//           }
//         })
//         .catch((error) => {
//           console.error('Error occurred while checking location permission:', error);
//         });
//     } else {
//       // Geolocation API not supported
//       window.alert('Geolocation is not supported by your browser.');
//     }
//   };
  
// const getlocation = () => {
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(
//         (position) => {
//           const latitude = position.coords.latitude;
//           const longitude = position.coords.longitude;
//           console.log('Latitude:', latitude);
//           console.log('Longitude:', longitude);
  
//           // You can also send the latitude and longitude to your Django view using AJAX
//           // Here's an example using jQuery:
//           $.ajax({
//             url: '/your-django-view-url/',
//             method: 'POST',
//             data: { latitude: latitude, longitude: longitude },
//             success: function (response) {
//               console.log('Data sent to Django successfully');
//             },
//             error: function (error) {
//               console.error('Error sending data to Django:', error);
//             },
//           });
//         },
//         (error) => {
//           console.log('Error getting location:', error.message);
//         }
//       );
//     } else {
//       console.log('Geolocation is not supported');
//     }
//   };

const getlocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;

            // Send the latitude and longitude data to the Django view using AJAX
            fetch('http://127.0.0.1:8000/store/nearest_hospitals/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}'  // Include CSRF token
                },
                body: JSON.stringify({ latitude: latitude, longitude: longitude })
            })
            .then(response => {
                // Handle the response from the Django view
                if (response.ok) {
                    console.log('Latitude and Longitude sent successfully!');
                    // Perform any further actions as needed
                } else {
                    console.log('Failed to send Latitude and Longitude!');
                }
            })
            .catch(error => {
                console.log('Error occurred while sending Latitude and Longitude:', error);
            });
        });
    }
};
