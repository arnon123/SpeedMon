class AppConfig {
  public readonly helloUrl: string = 'https://127.0.0.1:5000/api/hello';
  public readonly greetUrl: string = 'https://127.0.0.1:5000/api/greet/';
}

export const appConfig = new AppConfig();
