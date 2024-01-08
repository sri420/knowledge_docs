# How can I use AES GCM Encryption and Decryption in NodeJS?

Here is how you can use AES-GCM for encryption and decryption in Node.js:

First, install the crypto module:

```
npm install crypto
```

Then in your code:

Import the crypto module:

```js
const crypto = require('crypto');
```

Generate a random 256-bit key:

```js 
const key = crypto.randomBytes(32);
```

Define the initialization vector (IV). This should be random and unique:

```js
const iv = crypto.randomBytes(12);
```

Encrypt text using AES-GCM with the key, IV and additional authentication data (AAD):

```js
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let encrypted = cipher.update('Hello world', 'utf8', 'hex');
encrypted += cipher.final('hex');
const authTag = cipher.getAuthTag();
```

Decrypt the ciphertext using the same key, IV and authentication tag:

```js
const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
decipher.setAuthTag(authTag);
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');
```

The authentication tag is used to check data integrity. So the same key, IV and tag must be provided for decryption.

This uses the GCM mode which handles encryption and authentication in one step. The cipher outputs ciphertext and an auth tag which is used to verify integrity on decryption.


# What does additional authentication data (AAD) mean? With reference to the code shown where is it being used?

Additional authenticated data (AAD) refers to data that is authenticated but not encrypted. It is used to check the integrity and authenticity of data, but the data itself is not encrypted. 

In the code example, AAD is not being used. The 3rd parameter to `cipher.update()` and `decipher.update()` can be used to provide additional authenticated data.

For example:

```js
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

cipher.setAAD('additional data');

let encrypted = cipher.update('Hello world', 'utf8', 'hex'); 
// 'Hello world' is encrypted

encrypted += cipher.final('hex'); 

const authTag = cipher.getAuthTag();
```

And in decryption:

```js
const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);

decipher.setAAD('additional data'); // same AAD string
decipher.setAuthTag(authTag); 

let decrypted = decipher.update(encrypted, 'hex', 'utf8');

decrypted += decipher.final('utf8');
```

Here 'additional data' is authenticated but not encrypted. The receiver can verify that the AAD matches what was originally provided, but cannot decrypt it.

So AAD allows authenticating non-secret data along with the encrypted data using the auth tag. This binds the AAD to the ciphertext.


# When creating the cipher , what is the usage of IV and Random key?

The IV (initialization vector) and random key are both important components for encryption using AES-GCM in Node.js:

IV (Initialization Vector):

- The IV is a random sequence of bytes that is used to initialize the cipher. 

- It provides a starting point for encryption so that even if the same plaintext is encrypted twice, the ciphertext will be different each time.

- The IV does not need to be secret, but it should be unique for each encryption operation.

- In Node.js, we generate a random 12 byte IV using `crypto.randomBytes(12)`. 

- The same IV needs to be provided for decryption to correctly decrypt the ciphertext.

Random Key:

- The key is a 256-bit (32 byte) random sequence used as the encryption key for AES-GCM. 

- The key needs to be kept secret and ensures only those with the key can decrypt the ciphertext.

- In Node.js, we generate a random 32 byte key using `crypto.randomBytes(32)`.

- The same key needs to be provided for decryption to decrypt the ciphertext.

- If a different key is used, decryption will fail.

So in summary, the IV provides uniqueness and randomness to each encryption operation. The key provides secrecy and ensures only authorized parties can decrypt the data. Both are essential components for encryption/decryption using AES-GCM.


# Is there a way to use password hashing algorithms with AES GCM code in NodeJS?
Yes, it is possible to use password hashing with AES-GCM encryption in Node.js. 

Here is one way to do it:

1. Hash the password using a secure algorithm like bcrypt:

```js
const bcrypt = require('bcrypt');

const password = 'secret123';
const hashedPassword = await bcrypt.hash(password, 10);
```

2. Generate a 32-byte key from the hashed password: 

```js
const crypto = require('crypto');

const key = crypto.pbkdf2Sync(hashedPassword, 'salt', 10000, 32, 'sha512'); 
```

3. Use this key for AES-GCM encryption:

```js
const iv = crypto.randomBytes(12);

const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

// encrypt data...
```

4. To decrypt, hash the password again to derive the original key:

```js
const hashedPassword = await bcrypt.hash(password, 10);
const key = crypto.pbkdf2Sync(hashedPassword, 'salt', 10000, 32, 'sha512');

const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv); 

// decrypt data...
```

This ensures the key is derived from the password, and the password itself is not stored anywhere. The key can be re-generated each time for decryption by hashing the password.

You can use different hashing algorithms like Scrypt, Argon2 instead of Bcrypt based on your security needs.

# If instead of Bcrypt , we want to use Argon2 , how it can be done in nodejs?

Here is how you can use Argon2 instead of Bcrypt for password hashing with AES-GCM encryption in Node.js:

1. Install the argon2 module

```
npm install argon2
```

2. Hash the password using Argon2:

```js
const argon2 = require('argon2'); 

const password = 'secret123';

const hashedPassword = await argon2.hash(password); 
```

3. Generate the key from the hashed password:

```js
const crypto = require('crypto');

const key = crypto.pbkdf2Sync(hashedPassword, 'salt', 10000, 32, 'sha512');
``` 

4. Use the key for AES-GCM encryption/decryption

```js
// encrypt
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

// decrypt 
const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
```

5. To decrypt, re-hash the password with Argon2 to derive the original key:

```js 
const hashedPassword = await argon2.hash(password);
const key = crypto.pbkdf2Sync(hashedPassword, 'salt', 10000, 32, 'sha512'); 
```

So in summary, instead of Bcrypt, we use Argon2 for hashing the password before deriving the AES encryption key from it. The rest of the encryption/decryption process remains the same.

This provides enhanced security by using Argon2, which is more resistant to GPU cracking attacks compared to Bcrypt.

