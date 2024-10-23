# AWS

This is my AWS learning journey. I will be documenting the steps that I followed to create different AWS services.

## Register a new account
#### Registro en una Cuenta de AWS
Si no dispone de una Cuenta de AWS, siga estos pasos para crear una.

##### Procedimiento para registrarse en Cuenta de AWS
- Abra https://portal.aws.amazon.com/billing/signup.

- Siga las instrucciones que se le indiquen.

Parte del procedimiento de registro consiste en recibir una llamada telefónica e indicar un código de verificación en el teclado del teléfono.

Al registrarse en una Cuenta de AWS, se crea un Usuario raíz de la cuenta de AWS. El usuario raíz tendrá acceso a todos los Servicios de AWS y recursos de esa cuenta. Como práctica recomendada de seguridad, asigne acceso administrativo a un usuario y utilice únicamente el usuario raíz para realizar tareas que requieren acceso de usuario raíz.

AWS le enviará un email de confirmación cuando complete el proceso de registro. Puede ver la actividad de la cuenta y administrar la cuenta en cualquier momento entrando en https://aws.amazon.com/ y seleccionando Mi cuenta.

## AWS IAM Identity Center
This is the new section to admin the IAM users and groups recommended by AWS.
Create users and groups is basic to manage the permissions and policies.

Documentation: https://docs.aws.amazon.com/singlesignon/latest/userguide/set-up-single-sign-on-access-to-applications.html

Overview: https://docs.aws.amazon.com/es_es/lambda/latest/dg/getting-started.html This guide is useful to me.

#### Creación de un usuario con acceso administrativo
Después de registrarse para obtener una Cuenta de AWS, proteja su Usuario raíz de la cuenta de AWS, habilite AWS IAM Identity Center y cree un usuario administrativo para no utilizar el usuario raíz en las tareas cotidianas.

#### Protección de Usuario raíz de la cuenta de AWS
Inicie sesión en AWS Management Console como propietario de la cuenta; para ello, elija Usuario raíz e introduzca el correo electrónico de su Cuenta de AWS. En la siguiente página, escriba su contraseña.

Para obtener ayuda para iniciar sesión con el usuario raíz, consulte Iniciar sesión como usuario raíz en la Guía del usuario de AWS Sign-In.

#### Active la autenticación multifactor (MFA) para el usuario raíz.

Para obtener instrucciones, consulte Habilitación de un dispositivo MFA virtual para su usuario raíz de la Cuenta de AWS (consola) en la Guía del usuario de IAM.

#### Creación de un usuario con acceso administrativo
Activar IAM Identity Center.

Consulte las instrucciones en Activar AWS IAM Identity Center en la Guía del usuario de AWS IAM Identity Center.

En IAM Identity Center, conceda acceso administrativo a un usuario.

Para ver un tutorial sobre cómo utilizar Directorio de IAM Identity Center como origen de identidad, consulte Configuración del acceso de los usuarios con el Directorio de IAM Identity Center predeterminado en la Guía del usuario de AWS IAM Identity Center.

#### Iniciar sesión como usuario con acceso de administrador
Para iniciar sesión con el usuario de IAM Identity Center, utilice la URL de inicio de sesión que se envió a la dirección de correo electrónico cuando creó el usuario de IAM Identity Center.

Para obtener ayuda para iniciar sesión con un usuario del IAM Identity Center, consulte Inicio de sesión en el portal de acceso de AWS en la Guía del usuario de AWS Sign-In.

#### Concesión de acceso a usuarios adicionales
En IAM Identity Center, cree un conjunto de permisos que siga la práctica recomendada de aplicar permisos de privilegios mínimos.

Para conocer las instrucciones, consulte Create a permission set en la Guía del usuario de AWS IAM Identity Center.

Asigne usuarios a un grupo y, a continuación, asigne el acceso de inicio de sesión único al grupo.

Para conocer las instrucciones, consulte Add groups en la Guía del usuario de AWS IAM Identity Center.

## AWS CLI
The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts, this is very useful to me.

Documentation: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
I'm using the conffiguration for SSO (Single Sign-On) because I'm using the AWS IAM Identity Center (Recommended).

In order to configure the AWS CLI with SSO, I used the following command:
```bash
aws configure sso
SSO session name (Recommended): my-sso-christian
SSO start URL [None]: https://{your-aws-sso-start-url}.awsapps.com/start # Find this URL in Panel of IAM Identity Center
SSO region [None]: us-east-1 # The region of the AWS SSO instance (idk if this is the correct name)
SSO registration scopes [sso:account:access]: sso:account:access # This is the default value
Attempting to automatically open the SSO authorization page in your default browser.
If the browser does not open or you wish to use a different device to authorize this request, open the following URL:

https://device.sso.us-east-1.amazonaws.com/

Then enter the code:

FPVV-HBHC
The only AWS account available to you is:
Using the account ID 
The only role available to you is: AdministratorAccess # This is the role that I created in the AWS IAM Identity Center
Using the role name "AdministratorAccess"
CLI default client Region [None]: us-east-1 # The region of the AWS CLI
CLI default output format [None]: json # The output format of the AWS CLI (json, text, table, I wanna try use JSON)
CLI profile name [AdministratorAccess-40863]: chris-profile

To use this profile, specify the profile name using --profile, as shown:

aws s3 ls --profile chris-profile # Very important to use the profile name
```

This configuration is saved in the file `~/.aws/config`, we are able to edit when we want to change the configuration.

Other way to config is using the `aws configure` command:
```bash
aws configure sso-session --profile chris-profile
```

Add more sessions:
```bash
aws configure sso-session # I think this is the command but I'm not sure
```

# AWS SAM CLI
The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. With just a few lines per resource, you can define the application you want and model it using YAML. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster.

Documentation: https://docs.aws.amazon.com/es_es/serverless-application-model/latest/developerguide/install-sam-cli.html

AWS SAM CLI uses the AWS CLI configuration to interact with AWS services. If you have the AWS CLI installed, then you are ready to use the AWS SAM CLI.