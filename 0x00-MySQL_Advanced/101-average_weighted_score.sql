--Create procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id
    )
    WHERE id IN (SELECT user_id FROM corrections); -- Ensure to update only users who have corrections
END //
DELIMITER ;

