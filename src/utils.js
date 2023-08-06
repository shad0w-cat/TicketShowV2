export async function getUserRole() {
  try {
    const rawResponse = await fetch(
      `http://127.0.0.1:8081/api/getUserRole/${localStorage.getItem('userId')}`,
      {
        headers: {
          'access-token': localStorage.getItem('token'),
        },
      }
    );
    if (rawResponse.status === 200) {
      const userRole = await rawResponse.json();
      return userRole;
    } else {
      return null;
    }
  } catch (error) {
    console.error('New API call error:', error);
    return null;
  }
}
