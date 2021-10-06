# PTCGO-Code-Checker
Mass verify hundreds of PTCGO (Pokemon TCG Online) codes at once using this request based checker.

YOU MUST have a V2 Captcha solving service for this code checker to work as the Pkmn company requires a valid captcha token to validate PTCGO codes.
Through testing it appears that you can check as many codes as possible with the same captcha token until it expires. This means that you only need to generate one valid V2 captcha token every two mintutes.

Although the code checker still works it is still quite primitve and requires manual input of the codes to verify. You may have to tweak the code slightly for better functionality.

Reminder that this is still a work in progress which I may or may not update in the upcoming future.

POSSIBLE TODOs
- Add separate config files for mass code import/export
- Add discord webhook functionality for possible alerts
- Add an email scraper (Targeted for PTCGO sellers who mass receive hundreds of codes at a time)
