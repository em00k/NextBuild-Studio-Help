# F_WRITE ($9e)

## Description
Write bytes to file.

## Entry Parameters

| Register | Description |
|----------|-------------|
| `A` | File handle |
| `IX` | Address<br>(`HL` from dot command) |
| `BC` | Bytes to write |

## Exit Conditions

### Success
- `Fc=0`
- `BC=bytes actually written`

### Failure
- `Fc=1`
- `BC=bytes actually written`

## Links

https://gitlab.com/thesmog358/tbblue/-/tree/master/docs/nextzxos

