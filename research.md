# SELinux-Policy
Project Goal: develop an SELinux or set of SELinux policies that manage the permissions of a daemon

An assignment for COMP6841 23T3

# Week 1
Project ideation and planning

# Week 2
Begin research into SELinux Policies

## What is SELinux
Security Enhanced Linux (SELinux) provides an additional layer of system security. It aims to answer the question: May \<subject\> do \<action\> to \<object\>?
For example: May a webserver access files in users' home directories?

SELinux is a Mandatory Access Control (MAC) implementation.

## DAC vs MAC
Discretionary Access Control (DAC): security access control restricts access to objects based on the identity of the subject (the user). Implemented through
ACL lists, this is commonly used in Linux distros like the Unix file mode defines the read, write and execute permissions for an object for users.

Mandatory Access Control (MAC): security access control restricts access to objects based on the security labels of the object and the authorisation of the user.
Security labels are definition of the sensitivity of an object. They are composed of a security level and possibly a security category.

## How SELinux works
Every process or resource in a system is assigned a security label called an *SELinux context* or *SELinux label*. A context is the identifier for a resource used by an
SELinux policy to control access on that resource. SELinux policies enforce the access to resources by processes only if a policy rule exists. 

For example, when a process attempts to read a file, SELinux will intercept and consult the SELinux policy for the process to determine if the file allows that process to read
it. 

## SELinux label
SELinux labels are applied to all processes and files on systems running SELinux. Labels contain 4 fields:
1. user
2. role
3. type/domain
4. security level

Labels are stored in the form `<user>:<role>:<type>:<security level>`
For example, a file stored in the home directory will by default be assigned the label `unconfined_u:object_r:user_home_t:s0` 

### Confing Applications
Similar to accounts, applications must be confined to a SELinux type to enable rules to be enforced on them. For example, the `/etc/passwd` application has the label:
```bash
system_u:object_r:passwd_file_t:s0 /etc/passwd
```
This means it is confined to the type `passwd_file_t`. Normally, new applications are confined to the account's home type. Seeing the label associated with a compiled `c` file called basic:
```bash
unconfined_u:object_r:user_home_t:s0 basic
```
Whilst it has an unconfined SELinux user, the current user can still run this application as long as they are able to assume the `object_r` role which can interact with the `user_home_t` type.

However, lets say I created a system service and started it. As it is no longer present in the home directory (services live in the /usr/local/bin) directory, it will no longer be confined by the `user_home_t` type. Infact, it will be unconfined. For example, using a custom service called `mydaemon`, its label is:
```bash
system_u:system_r:unconfined_service_t:s0 root 4117    1  0 16:56 ?        00:00:00 /usr/local/bin/mydaemon
```
We can see it is now owned by the `system_u` user, however, it is not confined to a type. This means that the application is not enforced by any SELinux policies.


