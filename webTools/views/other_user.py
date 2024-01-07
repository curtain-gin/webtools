import re
from django.shortcuts import render, redirect, HttpResponse
from webTools.public.daba_tuple_to_dict import execute_query, other_query

import logging

logger = logging.getLogger("django")


def other_list(request):
    tille = "会员删除"
    if request.method == "GET":
        return render(request, "web/other_user.html", {"tille": tille})
    else:
        response_dict = request.POST.dict()
        if response_dict["phone"] == "" and response_dict["openid"] == "":
            """所有输入框为空"""
            return render(request, "web/other_user.html", {"tille": tille})
        elif response_dict["phone"] and response_dict["openid"]:
            """所有输入框有值"""

            return render(request, "web/other_user.html", {"tille": tille})

        elif response_dict["phone"] and response_dict["openid"] == "":

            """会员"""
            member_phone = response_dict["phone"]

            env_num = response_dict["select_environment"]
            print(env_num)
            try:
                sql = (
                    """
                    SELECT * FROM `res_usercore`.`u_official_user` 
                    WHERE `mobile` = %s   AND `is_deleted` ='0'
                    
                    """
                    % member_phone
                )

                result = execute_query(env_num, sql)
                for i in range(len(result)):
                    result[i]["env"] = env_num
                return render(
                    request, "web/other_user.html", {"pp": result, "tille": tille}
                )
            except Exception as e:
                logger.error(e)
                return render(request, "web/other_user.html", {"tille": tille})

        else:
            """会员openid"""
            try:
                non_members = response_dict["openid"]
                env_num = response_dict["select_environment"]
                sql = (
                    """
                    SELECT
                    *
                FROM
                    `res_usercore`.`u_user_weixin`
                WHERE
                    `openid` = '%s'
                    AND `is_deleted` = '0'
                    AND  `official_user_id`   IS NOT NULL
                ORDER BY
                    `official_user_id`
                """
                    % non_members
                )
                print(sql)
                result = execute_query(env_num, sql)

                for i in range(len(result)):
                    result[i]["env"] = env_num
                return render(
                    request, "web/other_user.html", {"pp": result, "tille": tille}
                )
            except Exception as e:
                logger.error(e)
                return render(request, "web/other_user.html", {"tille": tille})


def other_visitor_user_list(request):
    tille = "游客删除"
    if request.method == "GET":

        return render(request, "web/other_user_non.html", {"tille": tille})
    else:
        try:

            response_dict = request.POST.dict()
            non_members = response_dict["openid"]
            env_num = response_dict["select_environment"]
            sql = (
                """
                                SELECT
                                *
                            FROM
                                `res_usercore`.`u_user_weixin`
                            WHERE
                                `openid` = '%s'
                                AND `is_deleted` = '0'
                                AND  `official_user_id`   IS  NULL
                            ORDER BY
                                `official_user_id`
                            """
                % non_members
            )
            print(sql)
            result = execute_query(env_num, sql)
            for i in range(len(result)):
                result[i]["env"] = env_num
            return render(
                request, "web/other_user_non.html", {"pp": result, "tille": tille}
            )
        except Exception as e:
            logger.error(e)
        return render(request, "web/other_user_non.html", {"tille": tille})


def other_membersuser_delet(request, nid, env):
    tille = "会员删除"
    try:
        phone_re = "^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}"
        if re.match(phone_re, str(nid)):
            sql = (
                """
            UPDATE `res_usercore`.`u_user_weixin` 
        SET `is_deleted` = '1' 
        WHERE
            `official_user_id` = (
            SELECT
                `res_usercore`.`u_official_user`.`official_user_id` 
            FROM
                `res_usercore`.`u_official_user` 
            WHERE
                `mobile` = %s
                AND `is_deleted` = '0' 
            ) 
            """
                % nid
            )
            sql2 = (
                """
            
        UPDATE `res_usercore`.`u_official_user` 
            SET `is_deleted` = '1' 
        WHERE
            `mobile` = %s
            AND  `is_deleted` ='0'
            """
                % nid
            )
            other_query(env, sql)
            other_query(env, sql2)
            request_date = []
            ooooo = {"sql": sql, "sql2": sql2}

            request_date.append(ooooo)

            return render(
                request, "web/user_sql.html", {"pp": request_date, "tille": tille}
            )
    except Exception as e:
        logger.error(e)
        return render(request, "web/other_user.html", {"tille": tille})
        # return redirect('/other/user/list/')
    else:
        try:
            sql1 = (
                """
    
            UPDATE `res_usercore`.`u_user_weixin` 
                SET `is_deleted` = '1' 
            WHERE
                `openid` = '%s'
                AND  `is_deleted` ='0'
                AND `official_user_id` IS NOT NULL
                """
                % nid
            )
            sql2 = (
                """
                    UPDATE `res_usercore`.`u_official_user` 
                SET `is_deleted` = '1' 
                WHERE
                    `official_user_id` = (
                    SELECT
                        `res_usercore`.`u_user_weixin`.`official_user_id` 
                    FROM
                        `res_usercore`.`u_user_weixin` 
                    WHERE
                        `openid` = '%s'
                        AND `is_deleted` = '1' 
                        AND `official_user_id` IS NOT NULL
                        ORDER BY `created_time` DESC LIMIT 1
                    ) 
                    """
                % nid
            )

            other_query(env, sql1)
            other_query(env, sql2)
            request_date = []
            ooooo = {"sql": sql1, "sql2": sql2}

            request_date.append(ooooo)

            return render(
                request, "web/user_sql.html", {"pp": request_date, "tille": tille}
            )
        except Exception as e:
            logger.error(e)
            return render(request, "web/other_user.html", {"tille": tille})


def other_nom_user_delet(request, nid, env):
    tille = "游客删除"

    sql = (
        """

    UPDATE `res_usercore`.`u_user_weixin` 
    	SET `is_deleted` = '1' 
    WHERE
    	`openid` = '%s'
    	AND  `is_deleted` ='0'
    	AND `official_user_id` IS NULL
        """
        % nid
    )

    other_query(env, sql)
    request_date = []
    ooooo = {
        "sql": sql,
    }

    request_date.append(ooooo)

    return render(request, "web/user_sql.html", {"pp": request_date, "tille": tille})
