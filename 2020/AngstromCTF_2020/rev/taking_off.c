
int main(int param_1, long param_2)
{
  int iVar1;
  int uVar2;
  size_t sVar3;
  long in_FS_OFFSET;
  int local_b4;
  int local_b0;
  int local_ac;
  int local_a8;
  int local_a4;
  char *local_a0;
  byte local_98[136];
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  puts("So you figured out how to provide input and command line arguments.");
  puts("But can you figure out what input to provide?");
  if (param_1 == 5)
  {
    string_to_int(*(char **)(param_2 + 8), &local_b4);
    string_to_int(*(char **)(param_2 + 0x10), &local_b0);
    string_to_int(*(char **)(param_2 + 0x18), &local_ac);
    uVar2 = is_invalid(local_b4);
    if ((int)uVar2 == 0)
    {
      uVar2 = is_invalid(local_b0);
      if ((int)uVar2 == 0)
      {
        uVar2 = is_invalid(local_ac);
        if (((int)uVar2 == 0) && (local_ac + local_b0 * 100 + local_b4 * 10 == 0x3a4))
        {
          iVar1 = strcmp(*(char **)(param_2 + 0x20), "chicken");
          if (iVar1 == 0)
          {
            puts("Well, you found the arguments, but what\'s the password?");
            fgets((char *)local_98, 0x80, stdin);
            local_a0 = strchr((char *)local_98, 10);
            if (local_a0 != (char *)0x0)
            {
              *local_a0 = '\0';
            }
            sVar3 = strlen((char *)local_98);
            local_a4 = (int)sVar3;
            local_a8 = 0;
            while (local_a8 <= local_a4)
            {
              if ((local_98[local_a8] ^ 0x2a) != desired[local_a8])
              {
                puts("I\'m sure it\'s just a typo. Try again.");
                uVar2 = 1;
                goto LAB_00400bc7;
              }
              local_a8 = local_a8 + 1;
            }
            puts("Good job! You\'re ready to move on to bigger and badder rev!");
            print_flag();
            uVar2 = 0;
            goto LAB_00400bc7;
          }
        }
      }
    }
    puts("Don\'t try to guess the arguments, it won\'t work.");
    uVar2 = 1;
  }
  else
  {
    puts("Make sure you have the correct amount of command line arguments!");
    uVar2 = 1;
  }
LAB_00400bc7:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28))
  {
    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}

void string_to_int(char *param_1, undefined8 param_2)

{
  sscanf(param_1, "%d", param_2);
  return;
}

undefined8 is_invalid(int param_1)

{
  undefined8 uVar1;

  if ((param_1 < 0) || (9 < param_1))
  {
    uVar1 = 1;
  }
  else
  {
    uVar1 = 0;
  }
  return uVar1;
}
