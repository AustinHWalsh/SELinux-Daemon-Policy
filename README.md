# SELinux-Policy
Project Goal: develop an SELinux or set of SELinux policies that manage the permissions of a daemon

An assignment for COMP6841 23T3

# Week 1
Project ideation and planning

# Week 2
Begin research into SELinux Policies

## What is SELinux
Security Enhanced Linux (SELinux) provides an additional layer of system security. It aims to answer the question: May <subject> do <action> to <object>?
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
3. type
4. security level

Labels are stored in the form <user>:<role>:<type>:<security level> 
For example, a file stored in the home directory will by default be assigned the label unconfined_u:object_r:user_home_t:s0 

### SELinux users
In this section, the distinction between SELinux user and account are important. When talking about an account, it means the user logged into the system. For example,
by default on Fedora, *fedora* is the account. When executing a command with `sudo`, *root* is the account.
 
A SELinux user is an immutable field of the label used to audit and control access of the current account of the system. 
There exists multiple SELinux users:

* unconfined_u: SELinux user for unrestricted users. They have very few restrictions in applied to their user and is the default if an account is not mapped to a user. 
* root: The SELinux user for the root account
* sysadm_u: SELinux user with direct system admin role assigned
* staff_u: SELinux user for accounts that need to run both non-admin and admin commands. This is done through the staff_r and sysadm_r roles.
* user_u: SELinux user for non-admin accounts
* system_u: Special SELinux user for system services. It is not possible to directly use this user.

Accounts are mapped to a single SELinux user.
The SELinux users can be found using `semanage user -l`

### SELinux roles
