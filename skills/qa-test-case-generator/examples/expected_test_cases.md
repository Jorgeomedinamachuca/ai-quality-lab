# Expected Test Cases

| ID | Test Scenario | Preconditions | Steps | Expected Result | Priority | Risk Level | Test Type |
|---|---|---|---|---|---|---|---|
| TC-001 | Request password reset with registered email | User account exists | Enter registered email and submit reset request | Generic confirmation message is displayed | High | Medium | Functional |
| TC-002 | Request password reset with unregistered email | Email is not linked to an account | Enter unregistered email and submit request | Same generic confirmation message is displayed | High | High | Security |
| TC-003 | Submit invalid email format | None | Enter invalid email format and submit | Validation message is displayed | Medium | Low | Validation |
| TC-004 | Use expired reset link | Reset link has expired | Open expired reset link | User is informed that the link is invalid or expired | High | Medium | Functional |
| TC-005 | Create password that does not meet policy | Valid reset link exists | Enter weak password and submit | Password policy validation message is displayed | High | Medium | Validation |
| TC-006 | Complete reset and log in with new password | Valid reset link exists | Set valid new password and log in | User can log in with the new password | High | High | End-to-End |
| TC-007 | Check account enumeration protection | Registered and unregistered emails are available | Compare reset request messages for both emails | System does not reveal whether either email exists | High | High | Security |
