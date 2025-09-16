import express, { json, Request, Response } from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(json());

const port = process.env.PORT;

// oauth
const gooleOauthUrl = process.env.GOOGLE_OAUTH_URL;
const googleClientId = process.env.GOOGLE_CLIENT_ID;
const googleCallbackUrl = "http://localhost:4000/google/callback";
const googleOauthScopes = [
  "https://www.googleapis.com/auth/userinfo.email",

  "https://www.googleapis.com/auth/userinfo.profile",
];

// define the routes
// basic route to get authenticated first
app.get("/", async (request: Request, response: Response) => {
  const state = "some_state";
  const scopes = googleOauthScopes.join(" ");
  const googleOauthConsentScreenUrl = `${gooleOauthUrl}?client_id=${googleClientId}&redirect_uri=${googleCallbackUrl}&access_type=offline&response_type=code&state=${state}&scope=${scopes}`;

  response.redirect(googleOauthConsentScreenUrl);
});

// protected route only when logged in
app.get("/google/callback", async (request: Request, response: Response) => {
  response.send("<h1> Google Oauth Callback Url! </h1>");
});

// server running
app.listen(port, () => {
  console.log(`[server]:server is running on port http://localhost:${port}`);
});
