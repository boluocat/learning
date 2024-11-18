# Install Oracle19c on Windows

1. Download application and install it.

   Only install a DBA without create users.

   After installing process, configurate "database configuration assistant".



# Create users

When you have a new database, you did not have any users. Then you can create users.

1. connect to database

   ```cmd
   sqlplus /nolog
   ```

   ```SQL
   SQL> conn / as sysdba
   ```

2. create user

   ```SQL
   create user username identified by password;
   ```

3. alter password

   ```sql
   create user username identified by new_password;
   ```

4. drop user

   ```sql
   drop user username;
   ```

# grant a role to a user

There are three roles:

1. connect role

   A temporary user, it can visit table.

2. resource role

   User can create own table, sequence, procedure, trigger, index or cluster.

3. dba role

   A system role.

grant:

```sql
grant connect, resouce to username;
```

revoke:

```sql
revoke connect from username;
```

# make dba can be visited from internet

modify `listener.ora` and `tnsnames.ora`：

1. check host name of the computer

   ```cmd
   hostname
   ```

   If you want to rename computer name on Windows, you can rename it in the system page and restart it.

2. Modify `listener.ora` and `tnsnames.ora`. These two files are both under `db_home/network/admin` path:

   Change host part to your computer host.

3. restart oracle and listener.

   ```cmd
   sysplus /nolog
   ```

   ```sql
   conn sys / as sysdba
   ```

   ```sql
   shutdowm immediate
   startup
   ```